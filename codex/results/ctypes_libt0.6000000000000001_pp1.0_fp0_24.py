import ctypes
ctypes.cdll.LoadLibrary('libboost_python.so')

import pylab as plt
import numpy as np
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import time
from scipy.spatial import Delaunay
import cPickle
from mpl_toolkits.mplot3d import Axes3D
import scipy.io as sio
from scipy.optimize import leastsq
import cvxopt
from cvxopt import matrix, solvers, spmatrix
import random

def plot_3D(X, Y, Z, title):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(X, Y, Z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title(title)
    plt.show()

def plot_2D(X, Y, title):
    fig = pl
