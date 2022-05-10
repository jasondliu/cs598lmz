import weakref

from . import utils
from . import _compat as six
from . import _compat_pickle as pickle
from . import _compat_collections as collections
from . import _compat_collections_abc as collections_abc
from . import _compat_weakref as weakref

from . import _compat_collections_abc as collections_abc
from . import _compat_collections as collections
from . import _compat_weakref as weakref
from . import _compat as six
from . import utils
from . import _compat_pickle as pickle

__all__ = ['WeakKeyDictionary', 'WeakValueDictionary', 'WeakSet',
           'WeakMethod', 'WeakMethodProxy', 'WeakCallableProxyType']

#==============================================================================
# WeakKeyDictionary
