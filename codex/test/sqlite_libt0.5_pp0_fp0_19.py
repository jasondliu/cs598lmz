import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os
import sys

# set up logging
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


def get_db_path(db_name):
    if sys.platform == 'darwin':
        return os.path.join(
            os.path.expanduser('~'),
            'Library', 'Application Support',
            'Google', 'Chrome', 'Default', db_name
        )
    elif sys.platform.startswith('linux'):
        return os.path.join(
            os.path.expanduser('~'),
            '.config', 'google-chrome', 'Default', db_name
        )
