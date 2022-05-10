import mmap
import random
import traceback
import signal
import random
import errno
import platform

log = logging.getLogger(__name__)

NUM_RESULTS = 10
NUM_LINKS = 3
NUM_CATS = 3
MAX_KEYWORD_LENGTH = 50
MAX_DESCR_LENGTH = 100
MAX_TITLE_LENGTH = 20

class Filter:
    def __init__(self, filters, default_mode=None):
        self.filters = filters
        self.mode_map = dict()
        if default_mode is not None:
            self.mode_map['default'] = default_mode
        self.mode = self.mode_map['default']
    def _get_mode(self, user):
        return self.mode_map.get(user, self.mode_map['default'])
    def __call__(self, user, item):
        return self.filters[self._get_mode(user)](item)
    def clear(self, user):
        self.mode_map[user] = 'default'

