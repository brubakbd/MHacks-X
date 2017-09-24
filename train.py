
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.utils import np_utils
from util import load_data
import os.path
from keras.models import load_model



x_train, y_train = load_data()
x_train = x_train.astype('float32')
if os.path.isfile('trainModel.h5'):
    model = load_model('trainModel.h5')
else:
    print('good')
    model = Sequential()
    model.add(Dense(260, activation='sigmoid', input_shape=x_train.shape[1:]))
    model.add(Dropout(.5))
    model.add(Dense(2600, activation='sigmoid'))
    model.add(Dropout(.5))
    model.add(Dense(1, activation='sigmoid'))

model.compile(loss = keras.losses.mean_squared_error, optimizer = keras.optimizers.Adam())
model.fit(x_train, y_train, batch_size=10, epochs=1000, verbose=1, validation_data=(x_train, y_train))
score = model.evaluate(x_train, y_train, verbose = 0)
print(model.predict(x_train) - y_train)
model.save('trainModel.h5')