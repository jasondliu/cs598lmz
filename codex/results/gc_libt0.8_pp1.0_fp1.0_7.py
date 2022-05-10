import gc, weakref, warnings
from _weakref import ref, ReferenceType # py2/3 compat

from ._util import (
    is_cyclic_graph, clear_sentinels, clear_sentinels_for_gc,
    MAX_BLACK_LIST_LENGTH, MAX_CYCLE_LENGTH,
    get_full_name, look_for_old_items_in_o,
    )
from ._backports import _getfullargspec as getfullargspec
from ._deque import deque

_refs = {}

#===============================================================================
# Deal with Python 3 giving a warning if the objects sent in to weakref.ref()
# have a custom __hash__() without implementing __eq__()
#===============================================================================
_old_object_hash = object.__hash__

try:
    hash(object())
except TypeError:
    def hash(x):
        return _old_object_hash(x)

#===============================================================================
#
#===============================================================================

class CycleCollector(object):
    """
    The :class:`cyclecollector` collects
