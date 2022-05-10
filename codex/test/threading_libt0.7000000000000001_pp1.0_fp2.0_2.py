import threading
threading.stack_size(64*1024)

from spice import *
from spiceypy import *
from astro_constants import *
from toolbox import *
from vallado import *
from orb_elements import *
from orbital_elements import *
from satellite_data import *
from scipy.optimize import root
from scipy.optimize import fsolve
from scipy.optimize import minimize
import csv
from csv import writer
from pandas import DataFrame
from mpmath import *
import cmath

#%%
def main():
    
    #inputs
    kspice = '/Users/user/Documents/Kernels/kernel.txt'
    start_date = '2021 JAN 1'
    time_step = 10
    epoch_end = '2021 JAN 5'
    gm = 398600.4418
    mu = gm

    #load spice kernels
    loadKernel(kspice)
    
    #create ephemeris
