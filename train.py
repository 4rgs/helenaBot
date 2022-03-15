import tensorflow as tf
from data import X_train, y_train

# Hyper-parameters 
num_epochs = 2022 
batch_size = 12 
learning_rate = 0.0001
input_size = len(X_train[0])
hidden_size = 10
output_size = 10 


model = tf.keras.models.Sequential([
  tf.keras.Input(shape = input_size),
  tf.keras.layers.Dense(hidden_size, activation='relu'),
  tf.keras.layers.Dense(hidden_size, activation='relu'),
  tf.keras.layers.Dense(output_size, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=num_epochs)

model.summary()

model.save("helena")
