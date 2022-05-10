import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import modules
import os
import sys
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import matplotlib
import pylab
matplotlib.rcParams.update({'font.size': 9})

from matplotlib import style
style.use("ggplot")

# import own modules
from lib import get_stock_data
from lib import get_stock_data_yahoo
from lib import get_stock_data_yahoo_csv
from lib import get_stock_data_yahoo_csv_pandas
from lib import get_stock_data_yahoo_csv_pandas_fix
from lib import get_stock_data_yahoo_csv_pandas_fix_v2
from lib import get_stock_data
