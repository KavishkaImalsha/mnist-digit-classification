from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import SparseCategoricalAccuracy
from loading_data import loading_data
import joblib

def train_model():
    model = Sequential([
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

    X_train, Y_train, X_test, Y_test = loading_data()

    model.fit(X_train, Y_train, epochs=10)


    model.save('../models/Digit_classification.keras')

    return model

if __name__ == "__main__":
    train_model()