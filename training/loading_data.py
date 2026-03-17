import kagglehub
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def loading_data():
    #Load data from Kaggle
    path = kagglehub.dataset_download("bhavikjikadara/handwritten-digit-recognition")
    print(path)

    #Divide train and test data
    data = pd.read_csv(f'{path}/train.csv')
    train_data, test_data = train_test_split(data, test_size=40, shuffle=False)

    row, col = train_data.shape

    X_train = train_data.drop('label', axis=1)
    Y_train = train_data['label']
    X_test = test_data.drop('label', axis=1)
    Y_test = test_data['label']

    #Normalize data
    X_train = X_train / 255.0    
    X_test = X_test / 255.0

    return X_train, Y_train, X_test, Y_test
