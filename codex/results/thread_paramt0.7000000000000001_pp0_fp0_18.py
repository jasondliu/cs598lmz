import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
#import cv2
#from scipy.misc import imread, imsave, imresize
#from PIL import Image
import matplotlib.pyplot as plt
import time
import tensorflow as tf
import os
import csv
import sys
import random
import math
import re
import time
import numpy as np
import os
import sys
import cv2
import tensorflow as tf
import copy
import matplotlib
import gc

# Root directory of the project
ROOT_DIR = os.path.abspath("../../")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log

from samples.balloon import balloon

#%mat
