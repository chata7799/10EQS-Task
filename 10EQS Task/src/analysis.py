import pandas as pd
import requests
import os
from utils import clean_data, generate_insights

def main(csv_path):
    # Read and clean CSV data
    df = pd.read_csv(csv_path)
    df_cleaned = clean_data(df)
    
    # Fetch external data
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=COMMODITY_MONTHLY&symbol=COFFEE&apikey={api_key}'
    response = requests.get(url)
    commodity_data = response.json()
    
    # Generate insights
    insights = generate_insights(df_cleaned, commodity_data)
    
    # Write report
    with open('report.md', 'w') as f:
        f.write(insights)

if _name_ == "_main_":
    import sys
    main(sys.argv[1])