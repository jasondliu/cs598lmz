import weakref
import itertools
from dagtasets.types import *

_instances = weakref.WeakValueDictionary()

_type_checker = {
    'list': lambda x: isinstance(x, (tuple, list)),
    'tuple': lambda x: isinstance(x, tuple),
    'utf8': lambda x: isinstance(x, unicode) or (isinstance(x, bytes) and x.decode('utf8', errors='ignore')),
    'unicode_or_bytes': lambda x: isinstance(x, unicode) or isinstance(x, bytes),
    'utf8_or_utf16': lambda x: isinstance(x, unicode) or (isinstance(x, bytes) and (x.decode('utf8', errors='ignore') or x.decode('utf16', errors='ignore'))),
    'int': lambda x: isinstance(x, int), #PY2: int = long
    'bytes': lambda x: isinstance(x, bytes)
    }


