import threading
threading.stack_size(51200)

from flask import Flask, request, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import eventlet
eventlet.monkey_patch()

from model.model import Model
from model.trainer import Trainer

from keras.layers import Input, Dense, Lambda, Layer, Add, Multiply, Conv2D, MaxPooling2D, UpSampling2D, Flatten, Reshape
from keras.models import Model as KerasModel, Sequential
from keras.objectives import binary_crossentropy
from keras.callbacks import LearningRateScheduler

import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

import os
from os.path import join as pjoin

NUM_EPOCHS = 100
BATCH_SIZE = 32

MODEL_PATH
