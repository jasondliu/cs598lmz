import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import re
import sys
import os
import time
import datetime
import calendar
import argparse
import csv
import subprocess
import logging
import traceback
import requests
import json
import shutil
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
from matplotlib.backends.backend_pdf import PdfPages

from pylab import rcParams
rcParams['figure.figsize'] = 15, 10

import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
from matplotlib.dates import DateFormatter
from matplotlib.dates import MonthLocator
from matplotlib.dates import WeekdayLocator
from matplotlib.dates import MONDAY

from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import
