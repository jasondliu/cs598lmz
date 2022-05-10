import _struct
import _thread
import _threading
import _time
import _traceback
import _types
import _warnings
import _weakref

# Modules that are not available on all platforms
try:
    import _asyncio
except ImportError:
    pass
try:
    import _bisect
except ImportError:
    pass
try:
    import _collections
except ImportError:
    pass
try:
    import _contextlib
except ImportError:
    pass
try:
    import _copyreg
except ImportError:
    pass
try:
    import _datetime
except ImportError:
    pass
try:
    import _functools
except ImportError:
    pass
try:
    import _heapq
except ImportError:
    pass
try:
    import _imp
except ImportError:
    pass
try:
    import _io
except ImportError:
    pass
try:
    import _json
except ImportError:
    pass
try:
    import _locale
except ImportError:
    pass
try:
    import _
