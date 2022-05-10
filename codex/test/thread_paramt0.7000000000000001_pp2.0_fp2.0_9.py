import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from matplotlib import rc, cm
rc('text', usetex=True)

import os
import glob

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import h5py

from dedalus import public as de
from dedalus.extras.plot_tools import quad_mesh, pad_limits
from dedalus.extras import flow_tools

import logging
logger = logging.getLogger(__name__)

import time
start_time = time.time()

#from scipy.interpolate import RectBivariateSpline
from scipy.interpolate import interp2d

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

# Bases and domain
x_basis = de.Fourier('x', 1024, interval=(0, 4), dealias=3/2)

