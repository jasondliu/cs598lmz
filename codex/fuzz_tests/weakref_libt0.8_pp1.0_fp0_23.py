import weakref
from contextlib import contextmanager

from .. import channel, events
from .. import utils


class Database(object):

    def __init__(self, redis, namespace):
        self._client = redis
        self._namespace = namespace
        self._namespaced_key = lambda *args: self._namespace + ':' + ':'.join(args)

        self._logger = logging.getLogger(__name__)

    @property
    def namespace(self):
        return self._namespace

    def flush_db(self):
        keys = self._client.keys(self._namespace + ':*')
        if keys:
            self._client.delete(*keys)

    def get_num_total_games(self):
        return self._client.get(self._namespaced_key('num-total-games'))

    def update_num_total_games(self):
        return self._client.incr(self._namespaced_key('num-total-games'))

    def get_num_total_players(self):
        return self._
