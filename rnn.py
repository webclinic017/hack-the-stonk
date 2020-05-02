import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# Load the data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train = x_train / 255.0
x_test  = x_test  / 255.0

# Defining the type of model
model = Sequential()

# Defining the model
model.add(LSTM(128, input_shape = (28,28), activation = 'relu', return_sequences = True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation = 'relu'))
model.add(Dropout(0.1))

model.add(Dense(32, activation = 'relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation = 'softmax'))

opt = tf.keras.optimizers.Adam(lr=1e-3, decay = 1e-6)

# Compile the model
model.compile(loss = 'sparse_categorical_crossentropy',
              optimizer = opt,
              metrics = ['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs = 3, validation_data = (x_test, y_test))