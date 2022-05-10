fn = lambda: None
gi = (i for i in ())
fn.__code__ = 1, 2, 3, 4, 5, 6, 7, 8, 9
gi.gi_frame.f_code = fn.__code__
from sys import exc_info, _getframe
from inspect import getinnerframes, currentframe

from .test_support import check_warnings

from test import inspect_fodder

from types import FunctionType, BuiltinFunctionType
from types import TracebackType, FrameType


def test_getabsfile():
    # Make sure getabsfile() doesn't choke on various kinds of oddballs,
    # and returns a string for all sorts of objects.
    import inspect
    import test_importlib
    from test.test_importlib import SourcelessFileLoaderTests
    class Foo(object):
        pass
    assert inspect.getabsfile(Foo) is inspect.getabsfile(Foo())
    # This will fail if getabsfile() tries to import test_importlib.
    # That's what was happening in Python 2.7, but the fix started
    # with issue #10051 fixed that.
    assert inspect.getabsfile(test
