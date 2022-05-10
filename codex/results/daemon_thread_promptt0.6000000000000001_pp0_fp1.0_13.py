import threading
# Test threading daemon
import time
import traceback
import random
import string
import sys

# Logging
import logging
logger = logging.getLogger(__name__)

# Local imports
from . import config
from . import worker
from . import util
from . import lib
from . import db


def run():
    """
    Start all worker threads and run the main event loop.
    """
    # Create the main database
    db.create_database()

    # Start the DB thread
    db.start_db_thread()

    # Create the worker threads
    worker.create_workers()

    # Run the main event loop
    worker.run_event_loop()


def stop():
    """
    Stop all worker threads.
    """
    worker.stop_workers()
