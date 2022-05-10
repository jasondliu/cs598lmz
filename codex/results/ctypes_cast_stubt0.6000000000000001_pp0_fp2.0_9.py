import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
import platform

#print(sys.version)
print(platform.python_version())

import os
import pkg_resources
print(pkg_resources.get_distribution("numpy").version)
print(pkg_resources.get_distribution("pandas").version)
print(pkg_resources.get_distribution("scipy").version)

import numpy as np
print(np.__version__)
import pandas as pd
print(pd.__version__)
import scipy as sp
print(sp.__version__)

import math
print(math.__version__)

import matplotlib as mpl
print(mpl.__version__)
import matplotlib.pyplot as plt

import sklearn as sk
print(sk.__version__)
import sklearn.datasets as skd
import sklearn.linear_model as sklm
import sklearn.metrics as skm

import statsmodels as sm
print(sm.__version__)
import
