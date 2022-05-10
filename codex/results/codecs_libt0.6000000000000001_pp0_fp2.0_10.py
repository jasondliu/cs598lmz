import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import pandas as pd
# from pandas import DataFrame
import numpy as np
import os
import re
import datetime
import time
# import xlsxwriter
import xlrd
import openpyxl
import glob
import sys
import concurrent.futures
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style("whitegrid", {'axes.grid' : False})
import pprint
pp = pprint.PrettyPrinter(indent=4)

import warnings
warnings.filterwarnings('ignore')

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.l
