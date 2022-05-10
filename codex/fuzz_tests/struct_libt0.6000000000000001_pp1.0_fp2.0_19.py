import _struct
from collections import OrderedDict
from datetime import datetime
from functools import partial
from math import ceil, log
from os import path
from typing import Dict, List, Optional, Tuple, Union

import h5py
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.patches import Circle
from matplotlib.ticker import MaxNLocator
from scipy import signal
from scipy.interpolate import PchipInterpolator, lagrange
from scipy.signal import find_peaks
from scipy.stats import binned_statistic, linregress
from scipy.stats.mstats import gmean
from scipy.optimize import curve_fit

from .._utils import (
    _check_traces_dict,
    _convert_to_p
