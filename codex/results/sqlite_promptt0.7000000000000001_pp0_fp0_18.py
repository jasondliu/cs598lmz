import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/tmp/test.db')

import logging
import time
import re

from . import common
from . import file_handling
from . import constants as C
from . import db_sqlite3
from . import exceptions
from . import shared
from . import config
from . import db_sqlite3
from . import network_handling

from . import combinator


def _lock_db(log, db_conn):
    """Lock the database."""
    log.debug("Locking database")
    db_conn.execute("BEGIN IMMEDIATE TRANSACTION")
    log.debug("Database locked")


def _unlock_db(log, db_conn):
    """Unlock the database."""
    log.debug("Unlocking database")
    db_conn.commit()
    log.debug("Database unlocked")


def _run_sql(log, db_conn, sql_query, parameters=None):
    """Run SQL query, locking the database and unlocking it."""
    _lock_db(log, db_conn)
    try:
        if parameters:
