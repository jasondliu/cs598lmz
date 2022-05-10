import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

from matplotlib import animation
from IPython.display import HTML

import time

from scipy.integrate import odeint
from scipy.optimize import minimize

from scipy.interpolate import interp1d

import pandas as pd

import os

from scipy.optimize import curve_fit

from scipy.stats import norm

from scipy.stats import poisson

import random

from scipy.special import factorial

from scipy.special import erf

from scipy.stats import poisson

from scipy.stats import nbinom

from scipy.stats import binom

from scipy.stats import gamma

from scipy.stats import expon

