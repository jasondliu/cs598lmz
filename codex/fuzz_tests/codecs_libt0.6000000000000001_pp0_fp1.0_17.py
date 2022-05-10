import codecs
codecs.register(lambda name: codecs.lookup("utf-8") if name == "cp65001" else None)

# Imports
import sys
import os
import re
import csv
import time
import datetime
import math
import pprint
import traceback

# Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# Plotting
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter
from matplotlib.dates import MonthLocator
from matplotlib.dates import YearLocator
from matplotlib.dates import DayLocator
from matplotlib.dates import HourLocator
from matplotlib.dates import MinuteLocator

import matplotlib.patches as mpatches
import matplotlib.ticker as ticker

# Matplotlib Defaults
matplotlib.style.use('seaborn')


