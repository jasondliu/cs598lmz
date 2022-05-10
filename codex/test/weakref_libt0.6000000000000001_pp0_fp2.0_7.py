import weakref

import numpy as np
import pytest

import xarray as xr
from xarray.core.pycompat import PY3
from xarray.core.variable import as_variable, Variable, Coordinate
from xarray.core.dataset import Dataset
from xarray.core.groupby import GroupBy
from xarray.core.indexing import ExplicitlyIndexed
from xarray.core.duck_array_ops import allclose_or_equiv

from . import (
    assert_array_equal,
    assert_equal,
    assert_identical,
    assert_allclose,
    assert_array_almost_equal,
)


def test_as_variable():
    v = Variable(('x',), np.arange(10.0))
    v2 = as_variable(v)
    assert v is v2
    v3 = as_variable(v.values)
    assert_identical(v, v3)

    # test that attrs get copied
    v.attrs['foo'] = 'bar'
