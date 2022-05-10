import _struct
import _sys
import _thread
import _time
import _traceback
import _types
import _warnings
import _weakref
import _xxsubinterpreters
import _xxlimited
import _xxsubtype

# These modules are not available in restricted mode
if not _sys.flags.restricted:
    import _imp
    import _io
    import _locale
    import _pickle
    import _random
    import _sre
    import _string
    import _symtable
    import _testcapi
    import _threading_local
    import _tracemalloc
    import _winapi

# These modules are only available on Unix
if _sys.platform != "win32":
    import _posixsubprocess
    import _signal
    import _faulthandler
    import _posixshmem
    import _testbuffer
    import _testimportmultiple
    import _testmultiphase
    import _testcapi
    import _testcapimodule
    import _testcodecs
    import _testinternalcapi
    import _testjson
