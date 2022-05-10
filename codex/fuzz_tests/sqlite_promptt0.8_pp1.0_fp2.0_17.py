import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import os
import requests
from metadata_update_helper import *
from helpers import json_pretty_print
import datetime
from logging_helper import default_logger
from distutils.spawn import find_executable
from subprocess import Popen

# Mutex used to synchronize access to the metadata data structure
metadata_lock = threading.Lock()

# Public variables
sdk_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
database_dir = os.path.abspath(os.path.join(sdk_dir, "..", "database"))
# The metadata store filename
metadata_file = "metadata.db"
# The full path to the metadata store file
full_metadata_file_path = os.path.join(database_dir, metadata_file)

# Private variables
__logger = default_logger()
# Metadata store variable
__metadata = None


def get_metadata_store():
    """
    Get the metadata store for the current service. If the metadata store does not exist
