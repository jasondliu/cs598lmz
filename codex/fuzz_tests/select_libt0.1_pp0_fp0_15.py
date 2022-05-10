import select
import socket
import sys
import time
import threading
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version

class Server(object):
    def __init__(self, config):
        self.config = config
        self.log = log.get_logger(config)
        self.log.info("Starting server version %s", version.VERSION)
        self.log.info("Listening on %s:%d", config.host, config.port)
        self.log.info("Document root is %s", config.document_root)
        self.log.info("Maximum request size is %d bytes", config.max_request_size)
        self.log.info("Maximum number of headers is %d", config.max_headers)
        self.log.info("Maximum number of headers size is %d bytes", config.max_headers_size)
        self.log.info("Maximum number of keep-alive requests is %d", config.max_keepalive_requests)
        self.log.
