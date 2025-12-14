import os
import pandas as pd

def preprocess(input_file, output_file):
    # Load data
    df = pd.read_csv(input_file)

    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save preprocessed data
    df.to_csv(output_file, index=False)
    print(f"Data disimpan ke {output_file}")
    return df

if __name__ == "__main__":
    # Default paths (sesuaikan jika perlu)
    input_file = "dataset_raw\data_balita.csv"
    output_file = "preprocessing\data_preprocessed.csv"

    preprocess(input_file, output_file)
