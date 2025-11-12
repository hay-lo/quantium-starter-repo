import pandas as pd

# - Step 1: List your CSV files -
csv_files = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# - Step 2: Create a list to collect cleaned data -
dataframes = []
# - Step 3: Process each file -
for file in csv_files:
    print(f"Processing file: {file}")
    
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Clean up any stray spaces or casing issues in column names
    df.columns = df.columns.str.strip().str.lower()
    
    # Filter only rows for 'pink morsel'
    df = df[df['product'] == 'pink morsel']
    
    # Create a 'sales' column (quantity * price)
    df['sales'] = df['quantity'] * df['price']
    
    # Keep only the needed columns
    df = df[['sales', 'date', 'region']]
    
    # Add to our list
    dataframes.append(df)

# -Combine all three cleaned DataFrames -
final_df = pd.concat(dataframes, ignore_index=True)

# -Save the final formatted file -
final_df.to_csv('formatted_sales.csv', index=False)

dataframes.append(final_df)

print(final_df)