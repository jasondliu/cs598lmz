import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

import os
import time
import json
import numpy as np
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import save_image
from PIL import Image
from tensorboardX import SummaryWriter

from models.VAE import VAE
from models.VAE_LSTM import VAE_LSTM
from models.VAE_LSTM_CNN import VAE_LSTM_CNN
from models.VAE_LSTM_CNN_2 import VAE_LSTM_CNN_2
from models.VAE_LSTM_CNN_3 import VAE_LSTM_CNN_3
from models.VAE_LSTM_CNN_4 import VAE_LSTM_CNN_4
