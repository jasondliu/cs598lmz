import gc, weakref

from . import _base
from .. import _compat
from .. import _util
from .. import _exceptions
from .. import _types
from .. import _proxies
from .. import _proxy_list
from .. import _proxy_dict

from .._compat import PY2

if PY2:
    from UserDict import DictMixin
else:
    from collections import MutableMapping as DictMixin

class _DictProxy(_base._Proxy):
    __slots__ = ()
    def __init__(self, *args, **kwargs):
        raise TypeError("Cannot create '%s' instances" % self.__class__.__name__)

    def __getitem__(self, key):
        return self._get_object(key)

    def __setitem__(self, key, value):
        self._set_object(key, value)

    def __delitem__(self, key):
        self._del_object(key)

    def __len__(self):
        return self._get_length()


