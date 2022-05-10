import ctypes
import ctypes.util
import threading
import sqlite3
import itertools
import shlex

import mapnik
import cairo

import utils
import config
import database
import database.jobs
import database.maps
import database.tiles

_log = logging.getLogger(__name__)

###

class R:
    """
    Enumeration of render jobs statuses.
    """

    PENDING = 0
    RUNNING = 1
    STOPPED = 2
    FAILED = 3
    PAUSED = 4
    DONE = 5

###

class Renderer:
    """
    A class which provides an interface to the rendering system.
    """

    def __init__(self, pool, db, max_jobs=1, *args, **kwargs):
        """
        Initialize a new Renderer instance.

        pool: A multiprocessing.Pool instance which will be used to render tiles.
        db: A database.Database instance which will be used to access job data.
        max_jobs: Number of simultaneous rendering jobs.
        """

        self._pool = pool
