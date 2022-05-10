import gc, weakref
import sys
from collections import defaultdict
from contextlib import contextmanager
from functools import wraps

from . import _graph
from . import _utils
from . import _weakref
from . import _weakref_backports
from . import _weakref_weakkeydictionary
from . import _weakref_weakmethod
from . import _weakref_weakset

from . import _graph_weakref
from . import _graph_weakref_weakkeydictionary
from . import _graph_weakref_weakmethod
from . import _graph_weakref_weakset
from . import _graph_weakref_weakmethod_with_weakref


PY2 = sys.version_info[0] == 2
if PY2:
    import __builtin__ as builtins
else:
    import builtins


__all__ = [
    'get_referrers',
    'get_referents',
    'is_reachable',
    'get_reachable_objects',
    'get_backrefs',
]


def _get_weakref_module():
