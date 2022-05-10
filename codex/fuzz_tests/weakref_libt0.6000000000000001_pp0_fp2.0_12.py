import weakref

from . import _util

from . import _err
from . import _pylibmc
from . import _client
from . import _pools
from . import _behaviors
from . import _hash
from . import _consts
from . import _thread_util

MAX_RETRIES = 2

class Client(_client.Client):
    def __init__(self, servers,
                 binary=False,
                 behaviors=None):
        self.binary = binary
        self._behaviors = _behaviors.Behaviors(**behaviors or {})

        if isinstance(servers, (list, tuple)):
            servers = _pools.HashRing(
                [_util.server_key(s) for s in servers])
        elif isinstance(servers, dict):
            servers = _pools.HashRing(servers)
        elif not isinstance(servers, _pools.HashRing):
            raise _err.ProgrammingError("servers must be a list, tuple, or "
                                        "dictionary")

        self
