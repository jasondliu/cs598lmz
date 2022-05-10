import _struct
import _sys
import _thread
import _time
import _types
import _unittest
import _weakref

# These modules are not available on all platforms
try:
    import _audioop
except ImportError:
    pass
try:
    import _bisect
except ImportError:
    pass
try:
    import _codecs_cn
except ImportError:
    pass
try:
    import _codecs_hk
except ImportError:
    pass
try:
    import _codecs_iso2022
except ImportError:
    pass
try:
    import _codecs_jp
except ImportError:
    pass
try:
    import _codecs_kr
except ImportError:
    pass
try:
    import _codecs_tw
except ImportError:
    pass
try:
    import _csv
except ImportError:
    pass
try:
    import _ctypes
except ImportError:
    pass
try:
    import _ctypes_test
except ImportError:
    pass
try:
    import _element
