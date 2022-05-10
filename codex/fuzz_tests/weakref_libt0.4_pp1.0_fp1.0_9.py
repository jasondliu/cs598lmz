import weakref

from . import _util
from . import _util_py3 as _util3
from . import _errors as _errors_mod
from . import _errors_py3 as _errors_mod3
from . import _types as _types_mod
from . import _types_py3 as _types_mod3
from . import _threads as _threads_mod
from . import _threads_py3 as _threads_mod3
from . import _windows as _windows_mod
from . import _windows_py3 as _windows_mod3
from . import _winapi as _winapi_mod
from . import _winapi_py3 as _winapi_mod3

if sys.platform == 'win32':
    from . import _win32 as _win32_mod
    from . import _win32_py3 as _win32_mod3
    from . import _overlapped as _overlapped_mod
    from . import _overlapped_py3 as _overlapped_mod3
else:
    from . import _posix as _posix_mod

