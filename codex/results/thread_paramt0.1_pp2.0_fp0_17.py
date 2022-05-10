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

import random

import math

import copy

import pickle

import multiprocessing as mp

import itertools

import scipy.stats as stats

import scipy.special as special

import scipy.integrate as integrate

import scipy.optimize as optimize

import scipy.interpolate as interpolate

import scipy.spatial.distance as distance

import scipy.cluster.hierarchy as hierarchy

import scipy.cluster.vq as vq

import scipy.sparse as sparse

import scipy.sparse.linalg as
