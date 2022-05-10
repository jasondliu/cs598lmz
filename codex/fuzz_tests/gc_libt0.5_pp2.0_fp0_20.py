import gc, weakref
import numpy as np
import os
import pytest

from .. import normalize
from .. import util
from .. import wcs
from .. import wcs_util
from .. import wcs_utils
from . import helpers

try:
    import scipy
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

try:
    import pyregion
    HAS_PYREGION = True
except ImportError:
    HAS_PYREGION = False

try:
    import regions
    HAS_REGIONS = True
except ImportError:
    HAS_REGIONS = False


def test_wcs_util_overlap():
    w = wcs.WCS(naxis=2)
    w.wcs.ctype = ['RA---TAN', 'DEC--TAN']
    w.wcs.crval = [0, 0]
    w.wcs.crpix = [0, 0]
    w.wcs.cdelt = [1, 1]
    w.wcs.cunit = ['deg', 'deg']

