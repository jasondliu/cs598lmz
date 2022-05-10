import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import re
import glob
import os
import sys
import time
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
import string
from pprint import pprint 
import json
import numpy as np
from numpy import genfromtxt
import pandas as pd
from pandas import *
import random
from pandas import ExcelWriter
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from pandas import ExcelWriter
from pandas import ExcelFile
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import HourLocator
from matplotlib.dates import MinuteLocator
from matplotlib.dates import MonthLocator
from matplotlib.dates import MonthLocator
from matplotlib.dates import YearLocator
from matplotlib.dates import WeekdayLocator
from
