import threading
threading.stack_size(32768)
import time
import math
from pprint import pprint
import numpy as np
from math import atan2, degrees
from os import listdir
import os.path
import random
from random import shuffle
import json
import pandas
from sklearn.utils import shuffle
from datetime import datetime
from glob import glob
from pandas.io.json import json_normalize
from tqdm import tqdm

datadir = "/media/w/1c392724-ecf3-4615-8f3c-79368ec36380/DS Projects/Kaggle/Intel_Cervix/data/"
featdir = "/media/w/1c392724-ecf3-4615-8f3c-79368ec36380/DS Projects/Kaggle/Intel_Cervix/ML_data/cervix_classification_cropped_128_128/"

if not os.path.exists(featdir):
    os.mkdir(featdir)
