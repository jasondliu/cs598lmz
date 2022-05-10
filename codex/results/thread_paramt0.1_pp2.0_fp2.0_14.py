import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from IPython.display import HTML

import time

import os

import pandas as pd

import seaborn as sns

import matplotlib.gridspec as gridspec

from scipy.optimize import curve_fit

from scipy.stats import norm

from scipy.stats import gamma

from scipy.stats import poisson

from scipy.stats import nbinom

from scipy.stats import expon

from scipy.stats import lognorm

from scipy.stats import weibull_min

from scipy.stats import uniform

from scipy.stats import beta

from scipy.stats import exponweib

from scipy.
