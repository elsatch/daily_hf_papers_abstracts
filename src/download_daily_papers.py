import requests
import os
import sys
from datetime import datetime

def download_daily_papers(date=None):
    # If no date is provided, use today's date
    if date is None:
        date = datetime.now().strftime('%Y%m%d')
    
    # Convert YYYYMMDD to YYYY-MM-DD for the API
    formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
    
    # Construct the API URL
    url = f"https://huggingface.co/api/daily_papers?date={formatted_date}"
    
    # Create the data/input directory if it doesn't exist
    input_dir = os.path.join('data', 'input')
    os.makedirs(input_dir, exist_ok=True)
    
    # Construct the output filename
    output_file = os.path.join(input_dir, f"daily_papers_{date}.json")
    
    try:
        # Download the JSON file
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Write the content to the file
        with open(output_file, 'wb') as file:
            file.write(response.content)
        
        print(f"Successfully downloaded daily papers for {formatted_date} to {output_file}")
    except requests.RequestException as e:
        print(f"Error downloading daily papers: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If a date is provided as an argument, use it
        date = sys.argv[1]
        if not (len(date) == 8 and date.isdigit()):
            print("Invalid date format. Please use YYYYMMDD.")
            sys.exit(1)
    else:
        # Otherwise, use today's date
        date = None
    
    download_daily_papers(date)
