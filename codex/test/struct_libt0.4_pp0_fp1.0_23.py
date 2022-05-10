import _struct
import binascii
import os
import sys
import time
import zlib
import zmq

from lib.config import Config
from lib.logger import Logger

class ZMQServer(object):
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind('tcp://*:%s' % self.config.get('zmq', 'port'))
        self.logger.info('ZMQ server running on port %s' % self.config.get('zmq', 'port'))

