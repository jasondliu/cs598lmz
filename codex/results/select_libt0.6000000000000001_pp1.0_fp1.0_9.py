import select
import sys
import os
import time
import threading
import traceback
import base64
import json
import random

import numpy as np
import cv2

import mss
import mss.tools

from multiprocessing import Process, Pipe
from threading import Thread

from keras.models import load_model

import tensorflow as tf
from tensorflow.python.keras import backend as K

from .utils import preprocess_frame, print_screen, get_action_size, get_keys_to_action, get_action_meanings, get_n_actions
from .utils import key_check, keys_to_action, keys_to_onehot, onehot_to_key, get_action_name, get_action_number

from .config import Config

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_sct():
    with mss.mss() as sct:
        return sct

def screen_record(sct, pipe, config
