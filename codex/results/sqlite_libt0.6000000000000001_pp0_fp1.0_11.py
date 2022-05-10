import ctypes
import ctypes.util
import threading
import sqlite3
import zlib
import shutil
import re
import xml.etree.ElementTree as ET

from . import config
from . import utils
from . import db
from . import log

# -----------------------------------------------------------------------------

CONFIG_NAME = 'config.xml'

# -----------------------------------------------------------------------------
#
# log
#
# -----------------------------------------------------------------------------

logger = log.getLogger(__name__)

# -----------------------------------------------------------------------------
#
# config
#
# -----------------------------------------------------------------------------

class Config(object):

    def __init__(self, path):

        logger.debug("Load config in %s" % path)
        self.path = path
        self.config_path = os.path.join(path, CONFIG_NAME)

        self.config = config.Config(self.config_path)
        self.config.load()

        self.db_path = os.path.join(path, self.config.get('db', 'file'))
        self.db = db.DB(self.db_path)

        self.lock = threading.Lock()
        self.history_lock =
