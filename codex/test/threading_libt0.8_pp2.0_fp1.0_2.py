import threading
threading.stack_size(67108864) # 64MB stack

import os
import sys
import time

import matplotlib
matplotlib.use('Agg')

import numpy as np
import theano

import lasagne
import theano.tensor as T

from constants import *
from data_utils import *
from models import *
from experiment import *

