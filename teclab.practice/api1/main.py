
import numpy as np
import pandas as pd




def load_data(file_path):
    """
    Load data from a CSV file.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None



def preprocess_data(data):
    """
    Preprocess the data by handling missing values and normalizing numerical features.
    Args:
        data (pd.DataFrame): DataFrame containing the data to preprocess.
    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    
    
    data_titanic = load_data('titanic.data.csv')

    if data_titanic is None:
        return None

    print("Data loaded successfully. Preprocessing...")
    print(data_titanic.head())

    exit()
    

def main():
    # Tu código principal aquí
    preprocess_data(None)
    
if __name__ == "__main__":
    main()