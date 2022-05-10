import _struct
import _sys
import _thread
import _time
import _types
import _weakref

#
# The following modules are not builtin, but are included with the
# standard library.
#

import _codecs
import _collections
import _csv
import _functools
import _heapq
import _io
import _locale
import _random
import _socket
import _sre
import _string
import _struct
import _symtable
import _warnings
import _weakref

#
# These are builtin, but not necessarily always available
#

try:
    import _bisect
except ImportError:
    pass

try:
    import _hashlib
except ImportError:
    pass

try:
    import _md5
except ImportError:
    pass

try:
    import _sha
except ImportError:
    pass

try:
    import _sha256
except ImportError:
    pass

try:
    import _sha512
except ImportError:
    pass

