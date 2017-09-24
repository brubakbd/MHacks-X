
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.utils import np_utils
from util import load_data



x_train, y_train = load_data()
x_train = x_train.astype('float32')

model = load_model('savedModel')
model.fit(x_train, y_train, batch_size=10, epochs=1000, verbose=1, validation_data=(x_train, y_train))
model.save('savedModel')
score = model.evaluate(x_train, y_train, verbose = 0)
print(model.predict(x_train) - y_train)