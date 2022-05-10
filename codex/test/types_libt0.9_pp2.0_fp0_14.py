import types
types.SimpleNamespace
from desc.imsim import compare_obshistid_plots as compare_plots
import os
from astropy.io import fits
from desc.imsim import _fits_utils as f_utils
from desc.imsim import test_utils as tutils
import numpy as np
from scipy.stats import binned_statistic_dd, norm
import unittest
