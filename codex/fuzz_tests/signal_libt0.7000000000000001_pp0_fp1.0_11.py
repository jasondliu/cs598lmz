import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
from scipy.stats import chisquare

import readandcompute
import userinput
import pca

#------------------------------------------------------------------------------
#   PCA
#
#   Loads the data and calls the PCA function.
#------------------------------------------------------------------------------

def PCA():
    """PCA loading and computing"""
    global pca_data, pca_data_header, pca_data_orig, pca_data_x, pca_data_y, pca_data_z, pca_data_x_orig, pca_data_y_orig, pca_data_z_orig, pca_data_x_lim, pca_data_y_lim, pca_data_z_lim, pca_data_x_lim_orig, pca_data_y_lim_orig, pca_data
