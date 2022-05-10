import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref
import _weakrefset

# This is a list of modules that are known to be non-functional
# on App Engine.  This list should only include modules that
# are imported automatically by Python when certain functionality
# is requested.  A module should be added to this list only after
# it's confirmed that the module imports cleanly and then subsequently
# fails with some sort of functionality error (like AttributeError
# or ImportError).
_UNSUPPORTED_MODULES = [
    '_bsddb',
    '_codecs_cn',
    '_codecs_hk',
    '_codecs_iso2022',
    '_codecs_jp',
    '_codecs_kr',
    '_codecs_tw',
    '_csv',
    '_ctypes',
    '_curses',
    '_curses_panel',
    '_elementtree',
    '_hashlib',
