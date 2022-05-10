import types
# Test types.FunctionType
# Test types.ClassType
# Test types.TypeType
# Test types.InstanceType
# Test types.MethodType
# Test types.UnboundMethodType
import sys
# Test sys.getrefcount
import weakref
# Test weakref.proxy
import collections
# Test collections.namedtuple

try:
    import _winreg
except ImportError:
    import winreg as _winreg

from gi._gi import _API, Repository, PyGIDeprecationWarning, \
    PyGIWarning, PyGIDebugWarning, PyGIOverridesWarning, \
    PyGIApiWarning, PyGILogger
from gi._gi import _gobject, _gobject_property
from gi._gi import _glib
from gi._gi import _gideprecated
from gi._gi import _constants
from gi._gi import _error
from gi._gi import _enums
from gi._gi import _fields
from gi._gi import _gobject
from gi._gi import _gobject_property
from gi._
