import weakref

from . import _ffi as ffi
from . import _lib as lib

from . import _errors
from . import _util
from . import _compat
from . import _ffi
from . import _lib
from . import _types
from . import _version

from . import _lazy_loader
_lazy_loader.lazy_load_all()

from . import _lazy_loader
del _lazy_loader

if _compat.PY2:
    from . import _py2_compat
    from . import _py2_compat_collections
    from . import _py2_compat_functools
    from . import _py2_compat_itertools
    from . import _py2_compat_operator
    from . import _py2_compat_pickle
    from . import _py2_compat_threading
    from . import _py2_compat_weakref
    from . import _py2_compat_xmlrpc_client
    from . import _py2_compat_
