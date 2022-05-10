import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from utils import *
from data_loader import *
from model import *
from trainer import *
from evaluation import *
from visualization import *

from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
from matplotlib.pyplot import imshow

from IPython.display import clear_output

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

import warnings
warnings.filterwarnings("ignore")
 
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

print('TensorFlow version:', tf.__version__)

from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

print('TensorFlow version:', tf.__version__)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

from
