import ctypes
import ctypes.util
import threading
import sqlite3

from collections import OrderedDict
import textwrap

from gnutls.crypto import *
from gnutls.constants import GNUTLS_CIPHER_AES_128_CBC
import aprslib
from aprslib import parse

from . import logging_setup
from . config import Config

from .aprs_is.telnet import TnSocket
from .aprs_is.parse import *
from .aprs_is.ax25 import *

from .gnutls_crypto import *
from .sql import *


class LongDataWarning(Warning):
    pass

class NoCallsignReturned(Exception):
    pass

class UnknownCallsign(Exception):
    pass


logger = logging_setup.setup_logging()

def pretty_time(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


class MsgBuffer(object):

    def
