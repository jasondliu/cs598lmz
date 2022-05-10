import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref
import _weakrefset

# These modules are not built by default, but we still want to make sure
# that our import machinery can find them.
import _testbuffer
import _testimportmultiple
import _testinternalcapi
import _testmultiphase
import _xxsubinterpreters

# These modules should not be imported directly, but are still needed to
# support the import of other modules.
import _frozen_importlib
import _frozen_importlib_external
import _imp
import _io
import _py_abc
import _sitebuiltins
import _sysconfigdata
import _warnings
import _weakref

# These modules are only available on Windows.
if sys.platform == 'win32':
    import _overlapped
    import _winapi

# These modules are only available on Unix.
if sys.platform != 'win32':
    import _posixsubprocess
    import _scproxy
    import _signal
   
