import _struct
from . import lib
from .lib import ffi

from . import utils
from . import devutils
from . import lockfile
from . import bufferedwriter

# Default to reading form the config file
lib.leveldb_options_set_create_if_missing(options, 1)

###############################################################################

# FIXME: This is completely unsafe
class DictDB(object):
    def __init__(self, db):
        self.db = db

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        return self.exists(key)

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __repr__(self):
        return 'DictDB()'
