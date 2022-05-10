import weakref
import logging
import sys
import traceback
import os

from . import errors
from . import util
from . import constants
from . import events
from . import config

log = logging.getLogger(__name__)

class BaseConnection(object):
    """
    Base class for all connection types.
    """

    def __init__(self, host, port, user, password, database,
                 charset='utf8', ssl=False, ssl_keyfile=None, ssl_certfile=None,
                 ssl_ca=None, max_packet_size=16*1024*1024,
                 connect_timeout=None, read_timeout=None, write_timeout=None,
                 client_flags=constants.ClientFlag.get_default(),
                 cursorclass=util.DictCursor, init_command=None,
                 connect_attrs=None, autocommit=False,
                 read_default_file=None, read_default_group=None,
                 compress=False, named_pipe=False,
                 no_delay=False, auth
