import weakref

from . import _base
from . import _util
from . import _compat
from . import _errors
from . import _types
from . import _protocol
from . import _cython

from . import _cython

if _cython.compiled:
    from . import _cython_impl as _impl
else:
    from . import _python_impl as _impl

from . import _cython

if _cython.compiled:
    from . import _cython_impl as _impl
else:
    from . import _python_impl as _impl

from . import _cython

if _cython.compiled:
    from . import _cython_impl as _impl
else:
    from . import _python_impl as _impl

from . import _cython

if _cython.compiled:
    from . import _cython_impl as _impl
else:
    from . import _python_impl as _impl

from . import _cython

if
