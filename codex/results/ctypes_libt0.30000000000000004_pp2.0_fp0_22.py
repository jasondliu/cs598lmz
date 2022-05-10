import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import os
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.dates import YearLocator
from matplotlib.dates import HourLocator
from matplotlib.dates import MinuteLocator
from matplotlib.dates import SecondLocator
from matplotlib.dates import MONDAY
from matplotlib.dates import MO
from matplotlib.dates import TU
from matplotlib.dates import WE
from matplotlib.dates import TH
from matplotlib.dates import FR
from matplotlib.dates import
