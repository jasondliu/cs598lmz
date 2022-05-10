import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#------------------------------
# import modules
#------------------------------
import os
import sys
import glob
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.patches as mpatches
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.dates import YearLocator
import matplotlib.gridspec as gridspec
from matplotlib.offsetbox import AnchoredText
from matplotlib.offsetbox import TextArea
from matplotlib.offsetbox import AnchoredOffsetbox
from matplotlib.offsetbox import DrawingArea

