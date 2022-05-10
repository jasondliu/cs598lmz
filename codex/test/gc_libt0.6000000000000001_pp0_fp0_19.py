import gc, weakref
import sys
from threading import local

#===============================================================================
# PY3K:
#===============================================================================

if sys.version_info[0] == 3:
    import codecs
    from io import StringIO
    from itertools import zip_longest
    from functools import reduce
    from io import BytesIO

