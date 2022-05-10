import gc, weakref
import sys

import pytest

from greenlet import greenlet
from greenlet._util import wrap_ref, unwrap_ref


@pytest.fixture(autouse=True)
def enable_gc(request):
    """
    Enable garbage collection and make sure that every test case runs in its
    own garbage collection generation.
    """
    gc.enable()

    # The following is necessary to make sure that each test case runs in its
    # own garbage collection generation.
    gc.collect()
    gc_threshold = gc.get_threshold()
    gc.set_threshold(gc_threshold[0] + 1, gc_threshold[1], gc_threshold[2])

    def fin():
        gc.collect()
        gc.set_threshold(*gc_threshold)

    request.addfinalizer(fin)


def test_wrap_unwrap():
    x = object()
    x_ref = wrap_ref(x)
    assert unwrap_ref(x_ref) is x


def test
