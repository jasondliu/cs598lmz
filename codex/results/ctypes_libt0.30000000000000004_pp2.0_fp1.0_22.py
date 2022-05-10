import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
from matplotlib.colors import LogNorm
from matplotlib.colors import PowerNorm
from matplotlib.colors import Normalize
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator
from matplotlib.dates import MinuteLocator
from matplotlib.dates import SecondLocator
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.dates import YearLocator
from matplotlib.dates import WeekdayLocator
from matplotlib.dates import MO
from matplotlib.dates import T
