import weakref
import collections
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors as colors
from matplotlib import ticker
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import itertools
from scipy.stats import gaussian_kde
from scipy.stats import linregress
import os
import warnings
import time
import datetime
import cPickle as pickle
import json
import pprint
import glob
from collections import OrderedDict
from pandas import DataFrame, read_csv, concat
from scipy.stats import sem
import scipy.stats
import re
import sys
import subprocess
import pandas as pd
import seaborn as sns

from IPython.core.display import display,HTML

from IPython.core.debugger import Tracer; debug_here = Tracer()

#from IPython.core.debugger
