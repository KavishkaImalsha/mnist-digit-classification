from tensorflow.keras.metrics import SparseCategoricalAccuracy
def evaluate_model(model, X, Y):
    train_predictions = model.predict(X)

    acc = SparseCategoricalAccuracy()
    acc.update_state(Y, train_predictions)

    print(f'Accuracy {acc.result().numpy()}')
    
    acc.reset_state()