import select
import socket
import sys
import threading
import time

from . import log
from . import utils
from . import version

class Server:
    def __init__(self, config):
        self.config = config
        self.log = log.Log(config)
        self.log.info("Starting %s %s" % (config.name, version.VERSION))
        self.log.info("Listening on port %d" % config.port)
        self.log.info("Serving %s" % config.root)
        self.log.info("Using %d worker threads" % config.threads)
        self.log.info("Using %d bytes of memory per connection" % config.memory)
        self.log.info("Using %d bytes of disk cache" % config.cache_size)
        self.log.info("Using %s as the disk cache directory" % config.cache_dir)
        self.log.info("Using %s as the index file" % config.index)
