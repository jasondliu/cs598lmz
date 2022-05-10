import weakref

from . import _py2to3
from . import _utils
from . import _utils_py2
from . import _utils_py3
from . import _utils_posix
from . import _utils_win32
from . import _utils_osx
from . import _utils_linux
from . import _utils_freebsd
from . import _utils_openbsd
from . import _utils_netbsd
from . import _utils_sunos
from . import _utils_aix
from . import _utils_hpux
from . import _utils_sgi
from . import _utils_cygwin
from . import _utils_osf
from . import _utils_irix

from ._common import (
    AF_UNIX,
    AF_INET,
    AF_INET6,
    SOCK_STREAM,
    SOCK_DGRAM,
    SOCK_RAW,
    SOCK_RDM,
    SOCK_SEQPACKET,
    SOL_SOCKET,
    SO_REUSEADDR,
    SO
