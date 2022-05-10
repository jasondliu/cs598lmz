import weakref

from . import _core
from . import _util
from . import _py3compat

from . import _core
from . import _util
from . import _py3compat

try:
    from . import _cffi_ext
except ImportError:
    _cffi_ext = None

