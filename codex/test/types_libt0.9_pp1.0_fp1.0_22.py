import types
types.InstanceType = int
import multiprocessing
import matplotlib.pyplot as plt
from brian2 import *
import math
import numpy as np
import pandas as pd
import random as rd
#%matplotlib inline
#import os


#simulation parameters
simulation_time = int(0.1*second)
simulation_dt = float(0.025*ms)
defaultclock.dt = simulation_dt

#voltage recording parameters
n_ex_record_spines = int(10)
n_ex_record_dendrite = int(1)
n_in_record_spines = int(1)
n_in_record_dendrite = int(1)

n_ex_record_coordinate = np.arange(n_ex_record_spines)
n_in_record_coordinate = np.arange(int(100),100+n_in_record_spines)

#inhibitory neuron amplitudes and widths
inh_amp = 0.28
