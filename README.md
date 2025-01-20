# local-business-finder

This repository contains a Python script that leverages the Google Maps Geocoding and Places APIs to search for local businesses based on ZIP codes and keywords. Designed to streamline the process of finding businesses within a specified radius, the tool extracts business details such as name, address, and review count, and exports the data to a CSV file for further analysis.


**Key Features:** Geocoding: Convert ZIP codes into latitude and longitude coordinates. Business Search: Search for businesses using customizable keywords (e.g., landscaping, lawn care, hardscaping). Radius-Based Search: Define the search area in meters for precise targeting. Data Extraction: Extract business names, addresses, and review counts. CSV Export: Export results to a structured CSV file for reporting or analysis.

**Use Cases:** Market research for local businesses. Competitor analysis in specific industries. Identifying potential partners or clients in a geographic area.

**Requirements:** Python 3.x Google Maps API key with access to Geocoding and Places APIs.

**How to Use:** Update the `api_key` variable with your Google Maps API key. Set your desired ZIP code, radius, and keywords. Run the script to generate a CSV file with business details.
