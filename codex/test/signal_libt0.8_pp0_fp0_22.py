import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Other unnecessary things
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import sys
import h5py
import numpy as np
import time
import datetime
import traceback
import warnings
import epics
import math
import scipy.io as sio
from pkg_resources import parse_version

# Add my path
path = '/nfs/xf05id/sandbox/WS_GUI/'
sys.path.append(path)

# pv setting
# X-ray
