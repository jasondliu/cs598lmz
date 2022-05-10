import gc, weakref
import collections

from ._compat import OrderedDict, Mapping, MutableMapping
from ._compat import iteritems, itervalues, iterkeys
from ._compat import unichr, safe_unicode, int_types, iterbytes
from ._compat import str_types, string_types, byte_string_types

from . import base

#: Possible status when reading an object.
#:
#: - :obj:`None`: no status
#: - :const:`LOADED`: object is already loaded
#: - :const:`UNLOADED`: object needs to be loaded
#: - :const:`UNDEFINED`: object is not defined
#: - :const:`PARTIAL`: only few attributes of the object are loaded
LOADED = 'loaded'
UNLOADED = 'unloaded'
UNDEFINED = 'undefined'
PARTIAL = 'partial'

_sentinel = object()

class Collection(MutableMapping):

    '''A wrapper for working with a set of objects as a single
    instance.


