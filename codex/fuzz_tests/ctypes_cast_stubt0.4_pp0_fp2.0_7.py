import ctypes
ctypes.cast(0, ctypes.py_object)

# -----------------------------------------------------------------------------
# PyPy
# -----------------------------------------------------------------------------

try:
    import __pypy__
    _pypy = True
except ImportError:
    _pypy = False

# -----------------------------------------------------------------------------
# Jython
# -----------------------------------------------------------------------------

try:
    import org.python.core
    _jython = True
except ImportError:
    _jython = False

# -----------------------------------------------------------------------------
# IronPython
# -----------------------------------------------------------------------------

try:
    import System
    _ironpython = True
except ImportError:
    _ironpython = False

# -----------------------------------------------------------------------------
# Platform specifics
# -----------------------------------------------------------------------------

if is_pypy:
    from _pypy_platform import *
elif is_jython:
    from _jython_platform import *
elif is_ironpython:
    from _ironpython_platform import *
else:
    from _cpython_platform import *

# -----------------------------------------------------------------------------
# Python version
# -----------------------------------------------------------------------------

if is_pypy:
    from _pypy_version import *

