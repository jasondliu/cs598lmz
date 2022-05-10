import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection

from scipy.integrate import odeint
from scipy.optimize import minimize

from math import *

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from scipy.interpolate import griddata

from matplotlib.colors import LinearSegmentedColormap

import time

import os

import random

import copy

import pickle

import multiprocessing as mp

import itertools

import csv

import scipy.stats as st

import scipy.special as sp

import scipy.integrate as integrate

import scipy.interpolate as interpolate

import scip
