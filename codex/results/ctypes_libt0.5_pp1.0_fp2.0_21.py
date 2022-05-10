import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# import the necessary packages
from pyimagesearch.preprocessing import imagetoarraypreprocessor
from pyimagesearch.preprocessing import simplepreprocessor
from pyimagesearch.preprocessing import patchpreprocessor
from pyimagesearch.preprocessing import meanpreprocessor
from pyimagesearch.callbacks import trainingmonitor
from pyimagesearch.io import hdf5datasetgenerator
from pyimagesearch.nn.conv import resnet
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler
from keras.callbacks import ModelCheckpoint
from keras.callbacks import CSVLogger
from keras.optimizers import SGD
from keras.models import load_model
from keras.models import Model
from keras.layers import Input
from keras.utils import plot_model
from keras.utils import to_categorical
from sklearn.metrics import classification_report
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse

