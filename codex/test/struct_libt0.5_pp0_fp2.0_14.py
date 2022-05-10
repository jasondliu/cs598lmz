import _struct
import _sys
import _thread
import _time
import _threading
import _traceback
import _types
import _warnings
import _weakref
import _xxsubtype

# API extensions
import _testcapi
import _testbuffer
import _testimportmultiple
import _testinternalcapi
import _testmultiphase
import _testwinreg
import _tracemalloc
import _winapi

# Cleanup
import atexit
import gc
import os
import sys
import time

# Issue #7995: Avoid crash if unicodedata is not present
try:
    import unicodedata
except ImportError:
    unicodedata = None

# Issue #7996: Avoid crash if _multibytecodec is not present
try:
    import _multibytecodec
except ImportError:
    _multibytecodec = None

# Issue #7997: Avoid crash if _codecs_cn is not present
try:
    import _codecs_cn
except ImportError:
    _codecs_cn = None


