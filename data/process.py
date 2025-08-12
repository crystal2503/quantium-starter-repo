import pandas as pd
import os
csv_files = [
    'daily_sales_data_0.csv',
    'daily_sales_data_1.csv',
    'daily_sales_data_2.csv'
]

all_data = []

for file in csv_files:
    print(f"Processing {file} ...")
    df = pd.read_csv(file)
    df['product'] = df['product'].str.lower().str.strip()
    df['price'] = df['price'].str.replace('$', '', regex=False)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df = df.dropna(subset=['price', 'quantity'])
    df = df[df['product'] == 'pink morsel']
    df['sales'] = df['quantity'] * df['price']
    df = df[['sales', 'date', 'region']]
    all_data.append(df)
combined_df = pd.concat(all_data, ignore_index=True)
output_dir = os.path.join('..', 'output')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'pink_morsel_sales.csv')
combined_df.to_csv(output_file, index=False)
print(f"Done! Combined sales data saved to {output_file}")
