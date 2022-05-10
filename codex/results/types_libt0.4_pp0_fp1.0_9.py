import types
types.ModuleType.__repr__ = lambda self: self.__name__

import sys
import os
import re
import time
import tempfile
import shutil
import subprocess
import multiprocessing
import logging
import argparse
import traceback

import numpy as np
import scipy.stats

import pyximport
pyximport.install(build_in_temp=False, inplace=True)
import c_utils

import matplotlib.pyplot as plt

import pandas as pd

import sklearn.model_selection
import sklearn.metrics
import sklearn.linear_model
import sklearn.ensemble
import sklearn.svm

import statsmodels.api as sm
import statsmodels.formula.api as smf

import rpy2.robjects as ro

import seaborn as sns

import patsy

import pystan

import pymc3 as pm

import theano
import theano.tensor as tt

from collections import OrderedDict

import warnings
warnings.
