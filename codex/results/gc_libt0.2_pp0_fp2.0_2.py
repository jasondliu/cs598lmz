import gc, weakref
import numpy as np
import pytest

from numpy.testing import assert_array_equal, assert_array_almost_equal

from skimage import data
from skimage.util import img_as_float
from skimage.util.dtype import dtype_range
from skimage.util.shape import view_as_blocks
from skimage._shared import testing
from skimage._shared.testing import assert_equal, assert_array_equal_nulp
from skimage._shared.testing import assert_almost_equal
from skimage._shared.testing import assert_warns, assert_no_warnings
from skimage._shared.testing import assert_raises
from skimage._shared.testing import assert_raises_regex
from skimage._shared.testing import assert_warns_message
from skimage._shared.testing import assert_allclose_safely
from skimage._shared.testing import assert_allclose
from skimage._shared.testing import assert_allclose_nulp
from skimage._shared.testing import assert_allclose_nulp_safely
from skimage._shared
