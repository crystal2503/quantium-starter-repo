import pandas as pd
import os

# List of CSV files in the data folder
csv_files = [
    'daily_sales_data_0.csv',
    'daily_sales_data_1.csv',
    'daily_sales_data_2.csv'
]

all_data = []

for file in csv_files:
    print(f"Processing {file} ...")
    df = pd.read_csv(file)

    # Normalize product column: lowercase and strip spaces
    df['product'] = df['product'].str.lower().str.strip()

    # Remove $ sign from price and convert to float
    df['price'] = df['price'].str.replace('$', '', regex=False)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Convert quantity to numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

    # Drop rows with invalid price or quantity
    df = df.dropna(subset=['price', 'quantity'])

    # Filter only rows where product is exactly "pink morsel"
    df = df[df['product'] == 'pink morsel']

    # Calculate sales
    df['sales'] = df['quantity'] * df['price']

    # Select required columns
    df = df[['sales', 'date', 'region']]

    all_data.append(df)

# Combine all dataframes
combined_df = pd.concat(all_data, ignore_index=True)

# Output folder path (one level up from data)
output_dir = os.path.join('..', 'output')
os.makedirs(output_dir, exist_ok=True)

# Output CSV file path
output_file = os.path.join(output_dir, 'pink_morsel_sales.csv')

# Save combined dataframe to CSV without the index
combined_df.to_csv(output_file, index=False)

print(f"Done! Combined sales data saved to {output_file}")
