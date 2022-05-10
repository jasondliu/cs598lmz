import select
import socket
import sys
import time
import traceback
import threading
import random

from . import common
from . import config
from . import logger
from . import network
from . import protocol
from . import util
from . import version

from .common import *
from .config import *
from .logger import *
from .network import *
from .protocol import *
from .util import *
from .version import *

class Client:
    def __init__(self, config):
        self.config = config
        self.logger = logger.Logger(config)
        self.log = self.logger.log
        self.log_debug = self.logger.log_debug
        self.log_info = self.logger.log_info
        self.log_warning = self.logger.log_warning
        self.log_error = self.logger.log_error
        self.log_critical = self.logger.log_critical
        self.log_exception = self.logger.log_exception

