import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import sys
import time
import datetime
import argparse
import cv2
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torchvision.transforms as transforms
from torch.autograd import Variable
from PIL import Image

from models import *
from utils.utils import *
from utils.datasets import *
from utils.parse_config import *
from utils.utils import *

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_folder", type=str, default="data/samples", help="path to dataset")
    parser.add_argument("--config_path", type=str, default="config/yolov3.cfg", help="path to model definition file")
    parser.add
