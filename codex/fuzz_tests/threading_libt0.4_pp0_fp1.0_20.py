import threading
threading.stack_size(2**27)

import sys
import logging
import os
import random
import datetime
import time
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import matplotlib
import pylab
import tushare as ts
import talib
import urllib
import urllib.request
import json
import bs4 as bs
import pickle
import requests
import re
import csv
from pandas import DataFrame
from pandas_datareader import data as pdr
from pandas.tseries.offsets import BDay

import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.ops import gen_nn_ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import nn
