import mmap

from . import utils
from . import constants
from . import exceptions
from . import objects
from . import enums
from . import interfaces
from . import functions
from . import structures
from . import library
from . import types
from . import wrapper


class Session(interfaces.ISession):
    def __init__(self, context=None, user_type=None, user_data=None,
                 user_alloc=None, user_free=None, user_lock=None,
                 user_unlock=None, user_notify=None, user_logger=None):
        self.context = context
        self.user_type = user_type
        self.user_data = user_data
        self.user_alloc = user_alloc
        self.user_free = user_free
        self.user_lock = user_lock
        self.user_unlock = user_unlock
        self.user_notify = user_notify
        self.user_logger = user_logger

    @property
    def context(self):
        return self._context
