import select
import sys
import time

from . import util
from . import log
from . import config

class Socket(object):
    def __init__(self, sock, address, server):
        self.sock = sock
