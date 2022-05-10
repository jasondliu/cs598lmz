import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import xlog
from . import xlogviewer
from . import xlogviewer_pb2
from . import xlogviewer_rpc
from . import xlogviewer_server
from . import xlogviewer_util
from . import xlogviewer_web
from . import xlogviewer_web_pb2
from . import xlogviewer_web_rpc
from . import xlogviewer_web_server

from .xlogviewer_util import *

_logger = log.Logger('xlogviewer')

class XLogViewer(object):
    def __init__(self, config_file):
        self.config = config.Config(config_file)
        self.config.load()
        self.config.dump()

        self.xlog_viewer = xlogviewer.XLogViewer(self.config)
        self.xlog_view
