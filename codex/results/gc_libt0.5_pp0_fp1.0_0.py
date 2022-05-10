import gc, weakref
import numpy as np
from numpy.testing import assert_array_equal
import pytest

from skimage._shared._warnings import expected_warnings
from skimage.util import img_as_bool
from skimage.morphology import disk
from skimage.morphology import remove_small_objects, remove_small_holes
from skimage.morphology import (marching_cubes_lewiner,
                                marching_cubes_classic)
from skimage.transform import rescale


def test_remove_small_objects():
    a = np.array([[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0]], bool)

    b = remove_small_objects(a, 2)
    c = np.array([[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 1, 1,
