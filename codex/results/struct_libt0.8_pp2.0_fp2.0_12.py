import _struct
import _thread
import _threading_local
import _threading
import _traceback
import _tracemalloc
import _types
import _weakref
import _warnings
import _weakrefset
import _winapi
import _winreg
import _winxptheme
import _xxsubinterpreters
import _zlib


def _setup():
    # we setup the threading environment
    _thread._after_fork()
    _io._IOBase._after_fork()
    # we need to also setup the GUI environment
    _multiprocessing.multiprocessing._after_fork()


if hasattr(sys, 'setdlopenflags'):
    sys.setdlopenflags(_DLFCN_H)
_setup()
del _setup
