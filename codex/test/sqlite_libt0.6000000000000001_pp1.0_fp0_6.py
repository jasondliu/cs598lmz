import ctypes
import ctypes.util
import threading
import sqlite3
import hashlib
import shutil
import os.path

import logging

log = logging.getLogger(__name__)

from . import user

#
# Application settings
#

# Network settings

# Server settings

# User settings

_settings_path = os.path.join(user.app_data_path, 'settings.db')

if not os.path.exists(_settings_path):
    log.debug('Creating settings database: %s', _settings_path)
    shutil.copy2(os.path.join(user.app_data_path, 'settings.db.default'), _settings_path)

class Settings:
    def __init__(self, db):
        self.db = db
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def get(self, key, default=None):
        self.cursor.execute('SELECT value FROM settings WHERE key=?', (key,))
        row = self.cursor.fetchone()
