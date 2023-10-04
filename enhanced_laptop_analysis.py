
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load dataset from CSV file
def load_dataset_from_csv(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print("File not found. Please ensure the correct path is provided.")
        return None

# Function for data preprocessing steps
def data_preprocessing(data):
    data = data[data['release_year'].between(2020, 2023)]
    data['brand'] = data['product_name'].str.split(' ').str[0]
    return data

# Functions for data visualizations
def visualize_brand_distribution(data):
    # Code for visualizing brand distribution
    pass

def visualize_price_vs_display_size(data):
    # Code for visualizing price vs display size
    pass

# ... (other visualization functions)

if __name__ == "__main__":
    filepath = "YOUR_DATASET_PATH_HERE.csv"
    data = load_dataset_from_csv(filepath)
    if data is not None:
        data = data_preprocessing(data)
        visualize_brand_distribution(data)
        # ... (call other visualization functions)
