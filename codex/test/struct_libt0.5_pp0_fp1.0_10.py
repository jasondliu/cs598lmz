import _struct
import _time
import _types
import _unittest
import _urllib
import _weakref

# We need to import the Py3k warnings first so as not to confuse the
# warnings module.
import warnings as _warnings

_warnings.filterwarnings("ignore", "hex/oct constants", FutureWarning,
                         module="encodings")

# Now we need to remove the C:\Python30\lib\warnings.pyc file from
# sys.modules so that we can import the warnings module again.  (This is
# necessary because the py3k warnings module has the same name and lives
# in the same directory as the 2.x warnings module.)
if "warnings" in sys.modules:
    del sys.modules["warnings"]

import warnings
_warnings = sys.modules['_warnings'] = warnings

# We also need to override the builtin 'warnings' in __builtin__.
__builtin__.warnings = warnings

# Fix up some broken modules.
sys.modules['_strptime'] = _strptime
