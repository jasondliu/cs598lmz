import select
import socket
import sys
import traceback
import logging

from pydispatch import dispatcher

from common.config import Config
from common.events import *
from common.constants import *
from common.daemon import Daemon
from common.util import *

from worker import Worker
from worker_io import WorkerIO

class WorkerDaemon(Daemon):
    def __init__(self, pidfile):
        self.logger = logging.getLogger(__name__)
        Daemon.__init__(self, pidfile)

    def run(self):
        self.logger.info("Starting worker.")

        self.logger.debug("Creating I/O object.")
        self.io = WorkerIO()

        self.logger.debug("Creating worker.")
        self.worker = Worker(self.io)

        self.logger.debug("Registering signal handlers.")
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGINT, self.signal_handler)

        self
