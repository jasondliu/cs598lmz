import mmap
import re
import os
import sys
import random
import argparse
import logging
import string
import datetime
import time
import csv
import shutil
import copy
import collections
import math
import numpy as np
import pandas as pd
import multiprocessing as mp

import torch
import torch.nn as nn
from torch.utils import data
import torch.utils.data as Data
import torch.nn.functional as F
from torch.autograd import Variable
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence, pad_sequence

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

from tqdm import tqdm
from gensim.models import KeyedVectors

from utils import *
from preprocessing import *

