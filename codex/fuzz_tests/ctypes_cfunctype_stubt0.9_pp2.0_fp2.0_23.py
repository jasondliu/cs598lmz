import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ord(b'a')
use_pure_python = 0
if use_pure_python == 0:
    import sys
    import numpy as np
    from scipy.integrate import odeint
    import pylab as pl

    # import ros and rospy
    import rospy
    from sensor_msgs.msg import Range

    from matplotlib import cm
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.mlab as mb
    from matplotlib.ticker import LinearLocator, FormatStrFormatter

    from datetime import datetime
    import time

    import multiprocessing as mp
    from scipy.interpolate import interp1d
    from scipy.signal import butter, filtfilt

    import math
    import peakutils
    from peakutils.plot import plot as pplot
    import numpy
    class point_gen:
        def __init__(self, x_vals, y_vals=None, z_vals=None):
            self.
