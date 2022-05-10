import socket
import threading
import urllib.request
from datetime import timedelta
from threading import Thread
from fuzzywuzzy import fuzz
from spf import Sanity
from tinydb import where
from tinydb_serialization import SerializationMiddleware

from context import Context
from exceptions import NotConnected
from server import OpenProxyServer
from util import filename, User
from . import BadArgument, commands, get, group, is_owner, logging, set_default
from .config import CONFIG as c
from .models.db.banhammer import BanhammerDB
from .models.db.config import ConfigDB
from .models.db.report import ReportDB
from .util import DO_NOT_PING, get_channel, get_channel_context, get_channel_context_anywhere, get_user
from .util import log, log_command, owner, read_json, write_json

__all__ = ['admin', 'owner']

##
# Database setup

serialization = SerializationMiddleware()
serialization.register_serializer(User.serialize, User.deserialize)


