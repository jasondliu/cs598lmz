import gc, weakref
import sys
import traceback
import types

#------------------------------------------------------------------------------
# Utility functions
#------------------------------------------------------------------------------

def is_p3k():
    """Returns True if running under Python 3.0 or later."""
    return sys.version_info[0] >= 3

def is_pypy():
    """Returns True if running under PyPy."""
    return hasattr(sys, 'pypy_version_info')

def is_jython():
    """Returns True if running under Jython."""
    return sys.platform.startswith('java')

def is_cli():
    """Returns True if running under IronPython."""
    return sys.platform == 'cli'

def is_windows():
    """Returns True if running under Windows."""
    return sys.platform == 'win32'

def is_cygwin():
    """Returns True if running under Cygwin."""
    return sys.platform == 'cygwin'

def is_linux():
    """Returns True if running under Linux."""
    return sys.platform.startswith('linux')
