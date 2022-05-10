import mmap
import os
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from optparse import OptionParser

from pyinotify import WatchManager, Notifier, ProcessEvent, EventsCodes

from . import __version__
from . import utils
from . import config
from . import logger
from . import database
from . import indexer
from . import searcher
from . import web

class EventHandler(ProcessEvent):
    def __init__(self, db, indexer, searcher):
        self.db = db
        self.indexer = indexer
        self.searcher = searcher
        self.logger = logger.getLogger('EventHandler')

    def process_IN_CREATE(self, event):
        self.logger.debug('IN_CREATE: %s' % event.pathname)
        self.indexer.index(event.pathname)

    def process_IN_DELETE(self, event):
        self.logger.debug('IN_DELETE: %s' % event.
