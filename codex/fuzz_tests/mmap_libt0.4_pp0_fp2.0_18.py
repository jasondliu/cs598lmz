import mmap
import os
import sys
import time

from pymongo import MongoClient
from bson.objectid import ObjectId

from . import utils
from . import config
from . import log

from .utils import get_logger
from .config import get_config
from .log import get_log_dir

# TODO: add a timeout so that we don't wait forever for the file to be
#       written.

def is_locked(filepath):
    """Checks whether a file is locked by opening it in append mode.
    If no exception thrown, then the file is not locked.
    """
    locked = None
    file_object = None
    if os.path.exists(filepath):
        try:
            buffer_size = 8
            # Opening file in append mode and read the first 8 characters.
            file_object = open(filepath, 'a', buffer_size)
            if file_object:
                locked = False
        except IOError:
            locked = True
        finally:
            if file_object:
                file_object.close()

