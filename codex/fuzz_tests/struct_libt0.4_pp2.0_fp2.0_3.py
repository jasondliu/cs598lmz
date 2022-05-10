import _struct
import _sys
import _thread
import _time
import _unicodedata
import _warnings
import _weakref

# Import the builtins module, as some of its contents are used in the
# bootstrap process.
import builtins

# Import the _warnings module as a side-effect of importing the builtins module.
# This is needed because some of the bootstrap modules use the warnings module.
_warnings

# Setup the builtins module.
builtins.__name_ = '__main__'
builtins.__loader_ = None
builtins.__package_ = ''
builtins.__spec_ = None
builtins.__builtins__ = builtins
builtins.__doc__ = None
builtins.__name__ = '__main__'
builtins.__annotations__ = {}

# Import the bootstrap modules.
import _codecs
import _collections
import _functools
import _io
import _locale
import _operator
import _signal
import _sre
import _stat
import _string
import _symtable
import _
