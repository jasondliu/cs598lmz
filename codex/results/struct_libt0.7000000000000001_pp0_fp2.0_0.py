import _struct
import _sys
import _thread
import _time
import _types
import _unicodedata
import _warnings

# The C locale is always available.
import _locale

_locale.setlocale(_locale.LC_ALL, "C")

# Ensure that the builtins get removed from the __builtins__ module when
# it is no longer used.
import builtins
_sys.modules["builtins"] = builtins
del builtins

# Fix for Python bug #3221 (http://bugs.python.org/issue3221)
# This is needed to ensure that sub-interpreters ignore the main
# interpreter's option flags.
_sys.flags = _sys.get_config_vars().get("Py_FlagsStruct").split()

# Create a new interpreter
import _testcapi

subinterp = _testcapi.create_subinterpreter()

_sys.modules["subinterpreter"] = subinterp
del subinterp

# Make sure that the main interpreter can't see the sub-interpreter's
# modules, and
