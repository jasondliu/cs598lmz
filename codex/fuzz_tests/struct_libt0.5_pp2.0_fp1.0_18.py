import _struct
import _string
import _math
import _io
import _thread
import _imp
import _weakref
import _collections
import _random
import _bisect
import _heapq
import _pickle
import _datetime
import _functools
import _hashlib
import _operator

# TODO:
# - remove all "from _xx import *" from this file
# - replace all "from _xx import xxx" with "import _xx" and "xxx = _xx.xxx"

# the following modules are not available on Android

try:
    import _codecs
except ImportError:
    pass

try:
    import _locale
except ImportError:
    pass

try:
    import _multibytecodec
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
