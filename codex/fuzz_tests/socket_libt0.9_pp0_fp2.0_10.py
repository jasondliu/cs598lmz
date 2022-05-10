import socket
from random import randint
from time import sleep
from threading import Thread
from select import select
from . import botconfig
from .utils import threaded_task, send_request


PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_FILENAME = os.path.join(PLUGIN_DIR, 'logging.txt')


class SocketHandler(logging.Handler):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.log_cache = []

    def emit(self, record):
        log_entry = self.format(record)
        if botconfig.DEBUG_MODE:
            self.log_cache.append(log_entry)
        else:
            self._log(log_entry)

    def _log(self, log_entry):
        if self.client:
            self.client.msg(botconfig.CHANNEL, "10{0}".format(log_entry))

    def flush(self):
        for entry in
