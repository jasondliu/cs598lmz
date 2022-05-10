import gc, weakref
import numpy as np
import matplotlib.pyplot as plt
import pytest

from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS

from ..core import SkyImage, SkyCube
from ..core.utils import (
    _validate_input_data, _validate_input_wcs, _validate_input_unit)
from ..core.exceptions import (
    InputTypeError, InputArrayError, InputWcsError, InputUnitError)
from ..core.tests.helpers import make_wcsmap, make_wcsimage, make_wcscube
from ..core.tests.test_sky_image import make_test_image_file


@pytest.mark.parametrize(
    ('data', 'wcs', 'unit'),
    [(np.ones((10, 10)), None, 'm2'),
     (np.ones((10, 10)), make_wcsimage(), None),
     (np.ones((10,
