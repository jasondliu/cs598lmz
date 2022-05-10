import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import crypto
from . import database
from . import log
from . import message
from . import network
from . import protocol
from . import util

class Server(object):
    def __init__(self, config_file):
        self.config = config.Config(config_file)
        self.db = database.Database(self.config)
        self.log = log.Log(self.config)
        self.network = network.Network(self.config, self.log)
        self.protocol = protocol.Protocol(self.config, self.db, self.log, self.network)
        self.crypto = crypto.Crypto(self.config, self.db, self.log)
        self.message = message.Message(self.config, self.db, self.log, self.network, self.protocol, self.crypto)
        self.util = util.Util(self.config, self.db,
