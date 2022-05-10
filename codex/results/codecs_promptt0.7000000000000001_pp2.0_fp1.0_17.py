import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
try:
    codecs.register_error('strict', codecs.strict_errors)
except TypeError:
    pass

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import hashlib
import math
import os
import re
import sys
import threading
import time
import weakref
import xml.etree.cElementTree as ElementTree

import gdal
import osr

import numpy as np

from osgeo import gdal_array

from numpy.lib.recfunctions import append_fields

# This is to support NetCDF-3, which is not supported by the GDAL NetCDF driver.
# https://github.com/Unidata/netcdf-c/issues/102
try:
    from netCDF4 import Dataset
except ImportError:
    Dataset = None

# Define the logger.
_log = logging.getLogger(__name__)

# Define some
