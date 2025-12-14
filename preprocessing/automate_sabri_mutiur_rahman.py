import os
import pandas as pd

# Ambil root directory project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Path dataset (AMAN untuk Windows & Linux)
input_file = os.path.join(BASE_DIR, "dataset_raw", "data_balita.csv")
output_file = os.path.join(
    BASE_DIR, "preprocessing", "data_preprocessed.csv"
)

def preprocess():
    df = pd.read_csv(input_file)
    df.to_csv(output_file, index=False)
    print("Preprocessing selesai")

if __name__ == "__main__":
    preprocess()
