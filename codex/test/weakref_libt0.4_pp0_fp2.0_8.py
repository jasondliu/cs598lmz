import weakref

from . import _ffi
from . import _lib
from . import _py2_bytes
from . import _py2_chr
from . import _py2_unicode
from . import _py3_bytes
from . import _py3_memoryview
from . import _py3_unicode
from . import _py3_view
from . import _py_buffer
from . import _py_memoryview
from . import _py_slice
from . import _py_type
from . import _py_weakref
from . import _testcapi
from . import _types
from . import _warnings
from . import _weakref


def _test():
    import doctest
    import sys
    status = doctest.testmod(sys.modules.get("_ctypes_test"))
    if status[0]:
        raise Exception("failed")


