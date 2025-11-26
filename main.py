import pandas as pd
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

# Prepare the output file with header
header_written = False

# Loop through ALL CSV files in the directory
for file_name in sorted(os.listdir(DATA_DIRECTORY)):
    if not file_name.endswith(".csv"):
        continue

    file_path = os.path.join(DATA_DIRECTORY, file_name)
    print(f"Processing: {file_path}")

    # Read file in chunks to handle large datasets
    for chunk in pd.read_csv(file_path, chunksize=80_000):

        # Filter for pink morsel
        chunk = chunk[chunk["product"] == "pink morsel"]

        if chunk.empty:
            continue

        # Clean price ("$5" → 5.0)
        chunk["price"] = (
            chunk["price"]
            .str.replace("$", "", regex=False)
            .astype(float)
        )

        # Compute sales efficiently
        chunk["sales"] = chunk["price"] * chunk["quantity"].astype(int)

        # Keep only necessary columns
        chunk = chunk[["sales", "date", "region"]]

        # Append chunk directly to output CSV
        chunk.to_csv(
            OUTPUT_FILE_PATH,
            mode="a",
            index=False,
            header=not header_written
        )

        header_written = True

print("formatted_data0.csv created successfully (large-data optimized).")
