import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b]2;' + document.title + '\x07'))

#%%
# Import modules
import random
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
import copy
from copy import deepcopy
from IPython.display import clear_output
import time
import os
import sys
import logging
import pickle
import pandas as pd
import cv2
import datetime
import math
import time
import multiprocessing
import itertools
import scipy.stats
import scipy.signal
import scipy.spatial.distance
import scipy.interpolate
import scipy.optimize
from scipy.optimize import curve_fit
from scipy.optimize import least_squares
from scipy.optimize import minimize
import sk
