import _struct
from _socket import timeout
from time import time

from . import _compat, _compat_sock, _locale
from ._compat import (
    final,
    is_py2,
    is_py3_or_later,
    is_py34_or_later,
    is_pypy,
    is_pypy3,
    _memoryview,
    _unicode,
)
from ._compat_sock import (
    _AF_INET,
    _AF_INET6,
    _has_ipv6,
    _has_dualstack,
    _has_dualstack_ipv6,
    _SOCK_STREAM,
    _SOCK_DGRAM,
    _SOCK_RAW,
    _SOCK_SEQPACKET,
    _SOL_SOCKET,
    _SO_REUSEADDR,
    _SO_LINGER,
    _SO_ERROR,
    _SO_TYPE,
    _IPPROTO_IP,
    _IPPR
