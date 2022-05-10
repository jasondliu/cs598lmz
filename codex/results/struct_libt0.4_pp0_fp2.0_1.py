import _struct
import _sys
import _thread
import _time
import _types
import _unittest
import _warnings
import _weakref
import _zipfile
import _zlib

# Add in the standard C library modules.
import _codecs
import _collections
import _csv
import _functools
import _imp
import _io
import _locale
import _random
import _socket
import _sre
import _string
import _struct
import _symtable
import _thread
import _tracemalloc
import _weakref
import _winreg

# Add in the test support module.
import _testcapi

# Disable the import of the module that causes the regression test to fail.
_testcapi.import_in_test_should_fail = None

# Disable the import of the module that causes the test to hang.
_testcapi.import_in_test_should_hang = None

# Disable the import of the module that causes the test to crash.
_testcapi.import_in_test_should_crash = None

# Disable
