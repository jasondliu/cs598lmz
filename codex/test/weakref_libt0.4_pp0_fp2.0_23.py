import weakref

from . import _psutil_osx as cext
from . import _psutil_posix as cext_posix
from . import _psutil_posix as cext_posix
from ._common import memoize
from ._common import memoize_when_activated
from ._common import parse_environ_block
from ._common import sockfam_to_enum
from ._common import socktype_to_enum
from ._common import usage_percent
from ._compat import long
from ._compat import PY3
from ._compat import timeout_default
from ._compat import xrange
from .error import AccessDenied
from .error import NoSuchProcess
from .error import ZombieProcess
from .process import Process
from .process import _swapmem_info_ntuple
from .process import _virtual_mem_info_ntuple
from .process import _cached_phymem_info
from .process import _cached_virtmem_info
from .process import _cached_swapmem_info

__extra__all__ = []

# --- constants

AF_L
