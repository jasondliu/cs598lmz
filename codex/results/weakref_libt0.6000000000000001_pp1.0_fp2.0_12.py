import weakref

import numpy as np
import pandas as pd
import scipy.stats

import matplotlib as mpl
import matplotlib.cm
import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.path
import matplotlib.ticker
import matplotlib.transforms

import gvar

import lsqfit
import lsqfitgp2
import lsqfitgp2.plot

import util.colors
import util.layout
import util.plot
import util.root_finder
import util.statistics

import models
import models.data

# TODO:
#
# - add option to show only systematic errors on data
# - add option to show only statistical errors on data
# - add option to show only statistical errors on theory
# - add option to show theory and data with errors
# - add option to show data with errors only
# - add option to show theory only
# - add option to show theory with errors only
# - add option to show theory with errors only
# - add option to show theory with errors only

