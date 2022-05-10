import signal
# Test signal.setitimer
# Don't run on big endian as testonly for ia32
import platform
if platform.processor() != 'x86_64':
    raise ImportError("setitimer test only on 32bit platform")

from ctypes import *
from _ctypes_test import func1
import unittest

libc = CDLL(ctypes.util.find_library('c'))

def itimer_test(func):
    import _testcapi
    func.restype = c_ulong
    old = func(1, 0)
    try:
        signal.setitimer(signal.ITIMER_REAL, 10, 0)
        result = _testcapi.raise_itimer(signal.ITIMER_REAL, 1)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
        func(1, old)
    print result
    assert result == 1
    assert len(result)
    print result[0]
    assert isinstance(result[0], signal.ItimerError)


