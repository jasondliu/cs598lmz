import _struct
import _string
import _sys
import _types
import _thread
import _time

try:
    import _winreg
except ImportError:
    _winreg = None

try:
    import _winapi
except ImportError:
    _winapi = None

try:
    import _multiprocessing
except ImportError:
    _multiprocessing = None

# NOTE: _uuid is a Windows-specific, CFFI-based extension module, not a
# pure cpyext module.
try:
    import _uuid
except ImportError:
    _uuid = None

if sys.platform == 'win32':
    import _subprocess
    import msvcrt
    import _winxptheme
    import _msi

try:
    import _hashlib
except ImportError:
    _hashlib = None

try:
    import _random
except ImportError:
    _random = None

try:
    import _ssl
except ImportError:
    _ssl = None

try:
    import _ct
