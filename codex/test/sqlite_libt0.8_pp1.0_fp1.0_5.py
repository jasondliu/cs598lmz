import ctypes
import ctypes.util
import threading
import sqlite3
from SQLite_functions import *
from scapy.all import *

import multiprocessing
from multiprocessing import Process, Queue, current_process, freeze_support
from datetime import datetime, timedelta
import time
import os

from distutils.util import strtobool
from inspect import isclass
from random import uniform
import random

from statistics import mean, median
import statistics

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt



global pkt_counter
global payload_list
global data_list
global length_list


data_list = []
length_list = []
payload_list = []
pkt_counter = 0

NUM_PROC = 1

interval = 1
TIMEOUT = 2
curr_time = datetime.now()

class Data_Collector(object):
    def __init__(self):
        pass

   
