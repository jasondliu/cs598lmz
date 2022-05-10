import weakref

from . import _core
from . import _util
from . import _errors
from . import _types
from . import _lib
from . import _ffi
from . import _compat
from . import _version

__all__ = [
    'connect', 'connect_tcp', 'connect_unix', 'connect_uds', 'connect_memory',
    'connect_lmdb', 'connect_rocksdb', 'connect_stub', 'connect_embedded',
    'connect_embedded_rocksdb', 'connect_embedded_lmdb',
    'connect_embedded_memory', 'connect_embedded_stub',
    'connect_embedded_tcp', 'connect_embedded_unix', 'connect_embedded_uds',
    'connect_embedded_http', 'connect_embedded_https',
    'connect_embedded_http_proxy', 'connect_embedded_https_proxy',
    'connect_embedded_http_proxy_tls', 'connect_embedded_https_proxy_tls',
    'connect_
