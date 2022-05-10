import gc, weakref, operator
from collections import defaultdict
from itertools import chain
from . import _util, _compat
from ._util import is_bound_method, is_weakrefable
from ._compat import PY2, PYPY, PY3, _int_types, _iterkeys, _itervalues, _iteritems, _imap, _callable, _maxsize
from ._compat import _weakref_ref, _weakref_proxy, _weakref_getweakrefcount, _weakref_getweakrefs
from ._compat import _default_timer, _mod_name, _total_ordering, _get_ident, _get_module_name
from ._compat import _get_module_filename, _get_class_name, _get_method_name, _get_method_self
from ._compat import _get_method_function, _get_method_class, _get_method_closure
from ._compat import _get_function_code, _get_function_defaults, _get_function_globals
from ._compat import _get_function_
