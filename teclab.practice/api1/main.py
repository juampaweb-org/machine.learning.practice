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



    def search_null_data(self):
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
        
        return None
        
    def set_class_2_when_null(self):
        """
        Completes missing values in the 'pclass' column with 2.
        """
        if 'pclass' in self.dataset.columns:
            null_count = self.dataset['pclass'].isnull().sum()
            print(f"Cantidad de valores nulos en pclass: {null_count}")
            self.dataset['pclass'].fillna(2, inplace=True)
            print("Valores nulos en pclass completados con 2.")
        else:
            print("La columna 'pclass' no existe en el DataFrame.")
    

    def set_sex_correctly(self):
        """
        Sete correctamente los valores de la columna Sex para que solo exista male o female
        """
        if 'sex' in self.dataset.columns:
            # Mostrar valores únicos antes de la limpieza
            print("Valores únicos en la columna 'sex' antes de la limpieza:")
            print(self.dataset['sex'].value_counts(dropna=False))
            
            # Convertir a minúsculas para estandarizar
            self.dataset['sex'] = self.dataset['sex'].str.lower().str.strip()
            
            # Mapear valores similares a 'male' y 'female'
            sex_mapping = {
                'Hombre': 'male',
                'Mujer': 'female',
                'male': 'male',
                'female': 'female'
            }
            
            # Aplicar el mapeo
            self.dataset['sex'] = self.dataset['sex'].map(sex_mapping).fillna(self.dataset['sex'])
            
            # Mostrar resultado final
            print("\nValores únicos en la columna 'sex' después de la limpieza:")
            print(self.dataset['sex'].value_counts(dropna=False))
            
        else:
            print("La columna 'sex' no existe en el DataFrame.")


    def set_age_with_mean(self):
        """
        Completes missing values in the 'age' column with the mean age of the dataset.
        """
        if 'age' in self.dataset.columns:
            mean_age = self.dataset['age'].mean()
            print(f"Promedio de edad: {mean_age}")
            null_count = self.dataset['age'].isnull().sum()
            print(f"Cantidad de valores nulos en age: {null_count}")
            self.dataset['age'].fillna(mean_age, inplace=True)
            print("Valores nulos en age completados con el promedio.")
        else:
            print("La columna 'age' no existe en el DataFrame.")

    def set_s_in_null_embarked(self):
        """
        Completes missing values in the 'embarked' column with 'S'.
        """
        if 'embarked' in self.dataset.columns:
            null_count = self.dataset['embarked'].isnull().sum()
            print(f"Cantidad de valores nulos en embarked: {null_count}")
            self.dataset['embarked'].fillna('S', inplace=True)
            print("Valores nulos en embarked completados con 'S'.")
        else:
            print("La columna 'embarked' no existe en el DataFrame.")



def separador():
    print("\n" + "="*50 + "\n")

def main():
    data_titanic = DataPreprocessor('titanic.data.csv')
    
    # Punto a - Mostrar nulos
    data_titanic.search_null_data()
    separador()
    
    # Punto b - Completar valores NA en la columna Pclass
    data_titanic.set_class_2_when_null()
    separador()

    # Punto c - En la clase “Sex”, imputar los datos de manera de poder completar la
    # base solo con los valores “male” y “female”.
    data_titanic.set_sex_correctly()
    separador()

    # Punto d - d) En los casos de las personas de las cuales no se tenga la edad, rellenar
    # los datos con el promedio de edad de aquellos que sí tienen el dato.
    data_titanic.set_age_with_mean()
    separador()

    # En la columna embarked, asignar el valor “S” a aquellos datos que se
    # encuentran con valor vacío.
    data_titanic.set_s_in_null_embarked()
    separador()


if __name__ == "__main__":
    main()