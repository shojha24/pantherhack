import pandas as pd
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from PIL import Image


"""from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()"""


directory = "C:/Users/arhan/Downloads/faces-dataset"
folders = os.listdir(directory)
print(folders)

images = []
for folder in folders:
    folder_path = f"C:\\Users\\arhan\\Downloads\\faces-dataset\\faces-dataset\\{folder}"
    files = os.listdir(folder_path)
    for file in files:
        file_path = f"C:\\Users\\arhan\\Downloads\\faces-dataset\\faces-dataset\\{folder}\\{file}"
        with open(file_path, "rb") as f:
            img = Image.open(file_path)
            np_img = numpy.array(img)
            images.append(np_img)

print(images[0])
(x_train, y_train) = images
print(x_train.shape)
print(y_train.shape)

"""classification = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

y_train_one_hot = to_categorical(y_train)
y_test_one_hot = to_categorical(y_test)

x_train = x_train/255
x_test = x_test/255

model = Sequential()
model.add(Conv2D(32, (5,5), activation = 'relu', input_shape = (32,32,3)))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(32, (5,5), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Flatten())
model.add(Dense(1000, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(500, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(250, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

history = model.fit(x_train, y_train_one_hot, batch_size = 256, epochs=10, validation_split=0.2)

model.evaluate(x_test,  y_test_one_hot, verbose=2)
"""