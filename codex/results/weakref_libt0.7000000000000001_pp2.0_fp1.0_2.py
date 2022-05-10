import weakref

from twisted.internet import defer
from twisted.python import log

from deluge.core.authmanager import (
    AUTH_LEVEL_ADMIN,
    AUTH_LEVEL_NONE,
    AUTH_LEVEL_READONLY,
    AUTH_LEVEL_READWRITE,
    AUTH_LEVELS,
)
from deluge.core.rpcserver import (
    export,
    exceptions,
    register,
    REJECTED_BY_PLUGIN,
)

__all__ = ["AuthManager"]

log = logging.getLogger(__name__)


class AuthManager(object):
    def __init__(self, core):
        self.core = weakref.ref(core)
        self._auth_level_cache = {}
        self._auth_level_cache_expiry = {}

        self.__last_clean_time = time.time()

    @property
    def _core(self):
        return self.core()

    @defer.inlineCallbacks
    def _get_auth_level(self, user
