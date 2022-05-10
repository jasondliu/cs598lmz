import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time

from scipy.integrate import odeint
from scipy.optimize import minimize

from scipy.interpolate import interp1d

from scipy.stats import norm

import math

import random

import os

import pickle

import multiprocessing as mp

from scipy.stats import multivariate_normal

from scipy.stats import norm

from scipy.stats import uniform

from scipy.stats import gamma

from scipy.stats import beta

from scipy.stats import expon

from scipy.stats import poisson

from scipy.stats import binom

from scipy.stats import bernoulli

from scipy.stats import chi2

from scipy.stats import chi

