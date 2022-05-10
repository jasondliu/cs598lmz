import types
types.FunctionType = types.LambdaType

# import the necessary packages
from collections import OrderedDict
import numpy as np
import cv2
import time

# import the necessary packages
from tensorflow.keras.models import load_model
import os

# load the pre-trained model
print("[INFO] loading pre-trained network...")
model = load_model(args["model"])

# initialize the class labels dictionary
