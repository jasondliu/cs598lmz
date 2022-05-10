import _struct
import _thread
import _warnings
import _weakref

_sys.modules['sys'] = sys

__version__ = '0.0.1'

# -----------------------------------------------------------------------------
# The _io module, which depends on _pyio, is imported here to support the
# interactive interpreter when _pyio is not compiled in.
# -----------------------------------------------------------------------------

if _io is not None:
    _io.__name__ = 'io'
    _io.__package__ = ''
    _sys.modules['io'] = _io

# -----------------------------------------------------------------------------
# Import _thread if threads are enabled
# -----------------------------------------------------------------------------

del sys
