from keras.models import load_model

def predict(X):
    model = load_model('trainModel.h5')
    return model.predict(X)