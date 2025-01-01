import pandas as pd
import numpy as np

def preprocess_data(input_path, output_path):
    # Load data
    data = pd.read_csv(input_path)
    
    # Data preprocessing steps
    # Example: normalize, handle missing values, feature extraction
    data.fillna(0, inplace=True)
    data['normalized_feature'] = (data['feature'] - data['feature'].mean()) / data['feature'].std()
    
    # Save preprocessed data
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data("raw_data.csv", "preprocessed_data.csv")
