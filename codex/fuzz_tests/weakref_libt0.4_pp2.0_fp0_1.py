import weakref

from . import _cffi_backend
from . import _ctypes_backend
from . import _cython_backend
from . import _multiprocessing_backend
from . import _osx_backend
from . import _posix_backend
from . import _win_backend
from . import _windows_cffi_backend
from . import _windows_ctypes_backend

from ._posix_backend import _posix_sem_unlink
from ._posix_backend import _posix_sem_open
from ._posix_backend import _posix_sem_close
from ._posix_backend import _posix_sem_post
from ._posix_backend import _posix_sem_wait
from ._posix_backend import _posix_sem_trywait
from ._posix_backend import _posix_sem_timedwait
from ._posix_backend import _posix_sem_getvalue

from ._multiprocessing_backend import _multiprocessing_sem
