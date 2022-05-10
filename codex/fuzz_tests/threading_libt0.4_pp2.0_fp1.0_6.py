import threading
threading._DummyThread._Thread__stop = lambda x: 42

import os
import sys
import logging
import argparse
import json
import time
import pickle
import datetime
import traceback
import pprint
import random
import copy
import shutil
import logging
import logging.handlers
import signal
import subprocess
import re
import math
import csv
import cv2
import numpy as np
from collections import OrderedDict
import matplotlib
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
from torchvision import datasets, transforms
from torch.utils.data import Dataset, DataLoader

from tensorboardX import SummaryWriter

from torchvision import models
from torchvision import transforms

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall
