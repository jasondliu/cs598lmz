import mmap
import os
import re
import sys
import time

from . import util
from . import core
from . import log
from . import config
from . import constants
from . import exceptions
from . import server
from . import client

logger = log.getLogger(__name__)

class Server(server.Server):
    def __init__(self, address, port, key,
                 cert_file, cert_reqs, ca_certs,
                 ssl_version, ciphers,
                 do_handshake_on_connect, suppress_ragged_eofs,
                 server_side, certfile, keyfile):
        server.Server.__init__(self, address, port, key,
                               cert_file, cert_reqs, ca_certs,
                               ssl_version, ciphers,
                               do_handshake_on_connect, suppress_ragged_eofs,
                               server_side, certfile, keyfile)
        self.clients = {}
        self.client_count = 0
        self.client_
