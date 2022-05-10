import threading
threading.Thread(target=lambda: webbrowser.open('http://localhost:8888/notebooks/notebook.ipynb')).start()

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.optimizers import SGD
from keras.optimizers import Nadam
from keras.initializers import glorot_uniform
from keras.callbacks import Callback
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.callbacks import TensorBoard
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from keras.models import load_model
from keras.utils import to_categorical
