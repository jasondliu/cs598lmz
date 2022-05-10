import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

from scipy.integrate import odeint
from scipy.optimize import fsolve

from math import sqrt, pi, sin, cos, atan2

from time import sleep

from random import random

from copy import deepcopy

from collections import deque

from itertools import product

from multiprocessing import Process, Queue

from functools import partial

from tqdm import tqdm

from numba import jit

from scipy.spatial.distance import cdist

from scipy.optimize import minimize

from scipy.interpolate import interp1d

from scipy.stats import norm

from scipy.signal import savgol_filter


