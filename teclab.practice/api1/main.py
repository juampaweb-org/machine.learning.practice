import numpy as np
import pandas as pd



class DataPreprocessor:
    """Class for preprocessing data."""

    dataset = None

    def __init__(self, csv_file_titanic):
        self.dataset = self.load_data(csv_file_titanic)
        if self.dataset is None:
            raise ValueError("Failed to load the Titanic dataset.")
        

    def load_data(self, file_path):
        """
        Load data from a CSV file.
        Args:
            file_path (str): Path to the CSV file.
        Returns:
            pd.DataFrame: DataFrame containing the loaded data.
        """
        try:
            data = pd.read_csv(file_path)
            print("Data loaded successfully. Preprocessing...")
            if data.empty:
                print("Warning: The dataset is empty.")
                return None
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None



    def search_null_data(self, data):
        """
        Preprocess the data by handling missing values and normalizing numerical features.
        Args:
            data (pd.DataFrame): DataFrame containing the data to preprocess.
        Returns:
            pd.DataFrame: Preprocessed DataFrame.
        """
        missing_values = self.dataset.isnull().sum()
        print("Valores faltantes por variable:")
        print(missing_values)
        

def main():
    data_titanic = DataPreprocessor('titanic.data.csv')
    data_titanic.search_null_data(data_titanic.dataset)
    
if __name__ == "__main__":
    main()