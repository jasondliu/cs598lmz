import gc, weakref

from . import _util, _compat
from . import _util, _compat
from ._util import _b
from ._compat import PY3, xrange, text_type, binary_type, _int_types, _str_types, _iteritems, _items

if PY3:
    long = int

_unpickle_type = _compat.pickle.Unpickler

try:
    from cPickle import loads as c_loads
except ImportError:
    c_loads = None

_int_types = _compat._int_types
_str_types = _compat._str_types

try:
    from collections import OrderedDict
except ImportError:
    from . import _odict as OrderedDict

_have_namedtuple = True
try:
    from collections import namedtuple
except ImportError:
    _have_namedtuple = False

_have_collections_abc = True
try:
    from collections.abc import Mapping, MutableMapping, Sequence, MutableSequence
except
