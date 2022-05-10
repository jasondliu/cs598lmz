import threading
threading.stack_size(2**28)  # max stack size

# import Queue as queue
import queue as queue

import datetime
import os
import shutil
import time

import numpy as np
import pandas as pd

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

import statsmodels.api as sm
import statsmodels.tsa.stattools as ts

from config import (
    ALPHA_VANTAGE_API_KEY,
    DEFAULT_LOOKBACK_PERIOD_DAYS,
    MAX_DAYS_TO_WAIT_FOR_UPDATE,
    SYMBOL_LIST_PATH,
    TICKERS_DATA_DIR,
)

# from pandas_datareader import data
# import pandas_datareader as pdr

# from pandas_datareader.data import DataReader
# from pandas_datareader.famafrench import get_available_datasets

import matplotlib.pyplot as plt
