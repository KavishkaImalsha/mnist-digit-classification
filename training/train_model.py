from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from loading_data import loading_data
import joblib
from evaluation_model import evaluate_model

def train_model(evaluate=True):
    model = Sequential([
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

    X_train, Y_train, X_test, Y_test = loading_data()

    model.fit(X_train, Y_train, epochs=10)

    if evaluate:
        evaluate_model(model, X_train, Y_train)
        evaluate_model(model, X_test, Y_test)

    model.save('../models/Digit_classification.keras')

    print("Model save successfully")

    return model

if __name__ == "__main__":
    train_model()