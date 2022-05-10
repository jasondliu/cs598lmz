import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# The _weakref module is not built by default.  It is only needed for the
# weakref.proxy() function, which is rarely used.  If you do need
# weakref.proxy(), import _weakref and call _weakref.init() before using
# weakref.proxy().  _weakref.init() will raise ImportError if the _weakref
# module is not available.

# The _winreg module is only available on Windows.  It provides access to the
# Windows registry API.

# The _winapi module provides access to the Windows API.

# The _lsprof module provides a function for profiling Python code.

# The _testcapi module exposes the Python C API to the unittest module.

# The _testbuffer module provides unit tests for the buffer object.

