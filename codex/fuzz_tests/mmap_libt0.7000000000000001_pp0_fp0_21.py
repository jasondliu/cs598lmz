import mmap
import os
import sys
import time
from optparse import OptionParser
from numpy import *
from numpy.linalg import *

from pysynphot import extinction
from pysynphot import observation
from pysynphot import spectrum
from pysynphot import units

import fitsio
import uniq

from astropy.table import Table

from astropy.io import ascii
from astropy.io import fits

from astropy.wcs import WCS

from astropy.coordinates import SkyCoord
from astropy import units as u

import pyregion

from astropy.nddata.utils import extract_array
from astropy.nddata.utils import block_reduce

from ccdproc import ccd_process

from astropy.visualization import make_lupton_rgb

import photutils

from scipy.ndimage import gaussian_filter
from scipy import stats

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.patches import Rectangle

#from
