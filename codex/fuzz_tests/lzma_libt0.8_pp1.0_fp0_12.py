import lzma
lzma.LZMAFile

import numpy as np
import scipy as sp

from sys import argv, stdout
import matplotlib
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from scipy.spatial import cKDTree as KDTree
from scipy.special import eval_legendre

#from time import time

from hermite_library import *
import os

import h5py

#####
import matplotlib.animation as animation

__version__ = '1.1'

# DATA-DIR name
data_dir = '../data/'
c = 299792458.
# GRAVITATIONAL CONSTANT
G = 6.6726e-11 # m^3 / ( kg s^2 )

# FIXME:
dust_mass_density = 0.01 # kg/m^3

def get_gas_velocity(hf,with_kepler=True):
    gas_vel = np.zer
