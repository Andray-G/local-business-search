import requests
import pandas as pd
import os
import time

def get_lat_long(zip_code, api_key):
    geocode_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={zip_code}&key={api_key}'
    response = requests.get(geocode_url)
    results = response.json()

    if results['status'] == 'OK':
        location = results['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        raise Exception(
            f"Error retrieving coordinates for ZIP code: {results['status']} - {results.get('error_message', 'No error message')}"
        )

def get_businesses(lat, lng, radius, api_key, keyword):
    all_businesses = []
    places_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={api_key}'

    while places_url:
        response = requests.get(places_url)
        result = response.json()

        if 'results' in result:
            all_businesses.extend(result['results'])

        # Check for next page token
        next_page_token = result.get('next_page_token')
        if next_page_token:
            time.sleep(2)  # Wait to prevent throttling
            places_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={next_page_token}&key={api_key}'
        else:
            places_url = None

    return all_businesses

def main(zip_code, radius, api_key):
    try:
        # Get latitude and longitude for the ZIP code
        lat, lng = get_lat_long(zip_code, api_key)

        # List of keywords to search for
        keywords = [
            ### ADD KEYWORDS FOR SEARCH HERE (Ie."landscaping", "lawn care", "hardscaping", "landscapes", "hardscape", "hardscaper")]


        # Initialize a list to store business data
        business_list = []

        # Search for each keyword
        for keyword in keywords:
            businesses = get_businesses(lat, lng, radius, api_key, keyword)

            # Loop through the results and extract name, address, and review count
            for business in businesses:
                name = business['name']
                address = business.get('vicinity', 'No address provided')
                review_count = business.get('user_ratings_total', 0)

                # Append the business data to the list
                business_list.append({
                    'Business Name': name,
                    'Address': address,
                    'Review Count': review_count
                })

        # Create a pandas DataFrame
        df = pd.DataFrame(business_list)

        # Create folder if it doesn't exist
        os.makedirs('folder/subfolder', exist_ok=True)  # Create folder if not exist
        df.to_csv('###ADD FILEPATH', index=False)
        print(f'Data exported to with {len(business_list)} entries.')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    # Replace with your ZIP code and radius in meters (e.g., 30000 for 30 km)
    zip_code = "33578"
    radius = 100000  # 100 km
    api_key = "###ADD GGOGLE PLACES API KEY"  # Replace with your API key

    main(zip_code, radius, api_key)
