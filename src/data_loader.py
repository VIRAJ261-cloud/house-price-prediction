import pandas as pd
import numpy as np
import os

def load_data(filepath : str) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(
        f"Dataset Not found at: {filepath}\n"
        )
    
    df = pd.read_csv(filepath)
    print(f"data loaded of shape {df.shape[0]} rows * {df.shape[1]} columns")
    return df

def get_X_y(data: pd.DataFrame):
    X = data.drop(columns=['Order','PID','SalePrice'])
    y = data['SalePrice']
    return X,y