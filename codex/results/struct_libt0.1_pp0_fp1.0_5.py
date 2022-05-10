import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref
import _weakrefset

# Import the built-in modules.
import __builtin__
import _codecs
import _collections
import _csv
import _functools
import _imp
import _io
import _locale
import _operator
import _signal
import _sre
import _stat
import _string
import _symtable
import _thread
import _warnings
import _weakref

# Import the standard encodings.
import _codecs_cn
import _codecs_hk
import _codecs_iso2022
import _codecs_jp
import _codecs_kr
import _codecs_tw
import _codecs

# Import the site-specific modules.
# This call to imp.load_module() will import the *real* site module, not this
# fake one.
_site = _imp.load_module('site', *imp.find_module('site'
