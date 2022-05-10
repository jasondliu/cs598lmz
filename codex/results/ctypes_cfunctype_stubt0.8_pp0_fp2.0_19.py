import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 3
TestFailed('import ctypes failed')

try:
    import cPickle
except ImportError:
    import pickle as cPickle
TestFailed('import cPickle failed')

try:
    import zlib
except ImportError:
    zlib = None
    TestSkipped('import zlib failed')

try:
    import time
except ImportError:
    time = None
    TestSkipped('import time failed')

try:
    import hashlib
except ImportError:
    hashlib = None
    TestSkipped('import hashlib failed; python version is too old')

try:
    import math
except ImportError:
    math = None
    TestSkipped('import math failed')

try:
    import array
except ImportError:
    array = None
    TestSkipped('import array failed')

try:
    import _winreg
except ImportError:
    _winreg = None
    TestSkipped('import _winreg failed')

try:
    import thread
except ImportError:
    thread = None
    TestSkipped
