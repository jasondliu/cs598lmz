import gc, weakref
import numpy as np
import pytest
import pyopencl as cl
import pyopencl.array
import pyopencl.clrandom
import pyopencl.tools
import pyopencl.clmath
from pyopencl.tools import (  # noqa
        pytest_generate_tests_for_pyopencl as pytest_generate_tests)

import logging
logger = logging.getLogger("test_clmath")


def test_erf():
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    for dtype in [np.float32, np.float64]:
        for arg in [0, 0.5, 1, 1.5, 2]:
            res = pyopencl.clmath.erf(arg, dtype=dtype, queue=queue)
            assert res == pyopencl.clmath.erf(arg, dtype=dtype, queue=queue)
            assert res == pyopencl.clmath.erf(arg, dtype=dtype, queue=queue)

            assert
