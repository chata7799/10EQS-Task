import pandas as pd

def clean_data(df):
    df['our_price'] = df['our_price'].str.replace('$', '').astype(float)
    df['current_stock'] = pd.to_numeric(df['current_stock'], errors='coerce')
    df['restock_threshold'] = pd.to_numeric(df['restock_threshold'], errors='coerce')
    df['expiry_date'] = pd.to_datetime(df['expiry_date'], errors='coerce')
    df['category'] = df['category'].str.capitalize()
    return df

def generate_insights(df, commodity_data):
    coffee_products = df[df['product_name'].str.contains('Coffee', case=False)]
    avg_coffee_price = coffee_products['our_price'].mean()
    market_price = float(commodity_data['data'][-1]['value'])
    
    insight = f"# Product Pricing Analysis\n\n"
    insight += f"## Data Quality Issues\n"
    insight += f"- Missing values in 'restock_threshold' and 'current_stock'\n"
    insight += f"- Inconsistent date formats\n"
    insight += f"- Inconsistent capitalization in 'category'\n\n"
    
    insight += f"## Cleaned Data Summary\n"
    insight += f"- {len(df)} products analyzed\n"
    insight += f"- {len(coffee_products)} coffee products\n\n"
    
    insight += f"## External Data Integration\n"
    insight += f"- Current coffee commodity price: ${market_price:.2f}/lb\n\n"
    
    insight += f"## Business Insight\n"
    if avg_coffee_price > market_price:
        insight += f"Our average coffee price (${avg_coffee_price:.2f}/lb) is ${avg_coffee_price - market_price:.2f} higher than the current market price.\n"
    else:
        insight += f"Our average coffee price (${avg_coffee_price:.2f}/lb) is ${market_price - avg_coffee_price:.2f} lower than the current market price.\n"
    
    insight += f"\n## Recommendations\n"
    insight += f"1. Review coffee pricing strategy\n"
    insight += f"2. Monitor stock levels for products near restock threshold\n"
    insight += f"3. Standardize data entry processes for consistency\n"
    
    return insight