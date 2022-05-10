import weakref

import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
import healpy
from astropy.convolution import convolve, Gaussian2DKernel
from astropy.io import fits
from astropy.nddata import NDDataArray
from astropy.table import Table
from astropy.wcs import WCS
from astropy.wcs.utils import skycoord_to_pixel
from astropy.wcs.wcsapi import BaseHighLevelWCS
from numpy.random import randn
from scipy import interpolate
from scipy.ndimage import gaussian_filter, map_coordinates
from scipy.spatial import cKDTree
from scipy.stats import norm

from . import wcs_utils
from .exceptions import NoBeamException
from .fits_utils import read_header
from .hdu_utils import find_all_matching_hdu_types
from .region import Region, CircleSkyRegion
from .spectrum import SpectralCube
from .units import brightness_temperature_units, brightness_temperature
