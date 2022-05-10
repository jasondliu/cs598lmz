import threading
threading.stack_size(20000)

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import Response
from flask import send_file

from flask_cors import CORS

from werkzeug.utils import secure_filename

import os
import sys
import time
import json
import random
import shutil
import requests
import base64
import numpy as np
import cv2
from PIL import Image

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader

from sklearn.metrics import roc_auc_score

from utils import *
from model import *
from data import *

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------
# initialize our Flask application, Redis server, and Keras model
app = Flask(__name__)
CORS(app)

#
