import selectors

from url_shortener.common import utils
from url_shortener.common.exceptions import (
    InvalidConfiguration,
)
from url_shortener.common.log import logger


class TCPServer(object):

    def __init__(self, name, host, port, handler, backlog=100, reuse_port=False,
                 reuse_address=True, size=1024, max_connections=100,
                 max_messages=1000, max_age=60, max_idle=60):
        self.name = name
        self.host = host
        self.port = port
        self.handler = handler
        self.backlog = backlog
        self.size = size
        self.max_connections = max_connections
        self.max_messages = max_messages
        self.max_age = max_age
        self.max_idle = max_idle
        self.reuse_port = reuse_port
        self.reuse_address = reuse_address
        self.server = None
        self.clients = {}

