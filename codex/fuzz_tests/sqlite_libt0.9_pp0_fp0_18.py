import ctypes
import ctypes.util
import threading
import sqlite3
from uuid import uuid4
from time import time, sleep
from random import randint
from datetime import datetime
import socket
import bz2
from os import remove, rename
import os.path

from .util import stderr, stdout, ctrl_c, cleanup, get_peer_cert
from . import basic
from .master import is_ignored
from .global_var import GlobalVar
from . import proxy
from .local import Local
from .db import DB
from .git import Git
from .notifier import Notifier

from .client_key import ClientKey
from .client_cert import ClientCert

from . import crypto

from . import client_config
from .client_config import TRUSTED_CA_FILENAME_CLIENT, CONFIG_FILENAME, SERVER_FILENAME, CA_CN, default_root_url


class Client:
    def __init__(self, argv, local, g_var, db, git):
        self.argv = argv
        self.local = local
        self.g_var = g_
