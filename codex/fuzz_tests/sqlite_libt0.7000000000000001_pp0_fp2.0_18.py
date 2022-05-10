import ctypes
import ctypes.util
import threading
import sqlite3

from .handle import Handle, HandleError
from .log import Logger
from .config import Config
from .thread import Thread
from .database import Database

class Loader(Logger):
    def __init__(self):
        Logger.__init__(self, 'Loader')
        self.config = Config()

        self.handle = Handle(self.config.get_loader_handle())
        self.library_path = self.config.get_library_path()
        self.database_path = self.config.get_database_path()

    def run(self):
        self.logger.info('Loader started.')

        try:
            self.handle.open()
        except HandleError as e:
            self.logger.error('Handle error: {}'.format(e))
            return

        self.logger.info('Handle opened.')
        self.logger.info('Waiting for messages from driver.')

        self.threads = []

        try:
            while True:
                message = self.handle.read()
                if not message:
                   
