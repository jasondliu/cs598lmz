import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.gridspec as gridspec
from matplotlib.collections import PatchCollection
import matplotlib.cm as cm
import scipy.signal as signal
import scipy.optimize as optimize
import scipy.interpolate as interpolate
import scipy.ndimage as ndimage
import scipy.stats as stats
import scipy.io as io
import scipy.special as special
import time
import os
import random
import glob
import warnings
import h5py
import json
import argparse
import datetime
import traceback
import subprocess
import multiprocessing
import threading
import queue
import copy
import collections
import pickle
import time
import logging
import logging.handlers
import logging.config

