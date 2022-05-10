import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# These modules are not built by default, but we still want to make sure
# they are importable.

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
    import _collections
except ImportError:
    pass

try:
    import _csv
except ImportError:
    pass

