import gc, weakref
from functools import update_wrapper
import functools
from . import _compat
from . import _generic
from . import _type
from . import _signature
from . import _classregistry

# See the "Technical Details" section in _classregistry.rst
_registry_get_item_cache = weakref.WeakKeyDictionary()
# See the "Technical Details" section in _classregistry.rst
_registry_set_item_cache = weakref.WeakKeyDictionary()
_registry_set_item_cache_lock = threading.Lock()

_unpack_classes = functools.partial(_generic._unpack_generic,
                                    hook = lambda args: _type.get_origin(_type.select_parameters(args[0])))

# TODO This needs a full rewrite for the 2.4 branch because we are not
# careful about the constrains anymore.  That's why the handling of
# operands is different from the one from callables; in the callables
# case we assume that we can use class.__init__
