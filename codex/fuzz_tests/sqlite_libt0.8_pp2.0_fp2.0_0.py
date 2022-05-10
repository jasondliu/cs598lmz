import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
import re

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

FLT_EVENT_MASK = (
    bsddb.DB_LOCK_DEADLOCK |
    bsddb.DB_EVENT_REP_CLIENT |
    bsddb.DB_EVENT_REP_MASTER |
    bsddb.DB_EVENT_REP_NEWMASTER |
    bsddb.DB_EVENT_REP_STARTUPDONE |
    bsddb.DB_EVENT_WRITE_FAILED |
    bsddb.DB_EVENT_PANIC
)

REP_SYNC_PERIOD = 1
REP_RETRIES = 3

db_env = None

class Replication(object):

    def __init__(self, path, database, host, port, mhost, mport, group_id, num_clients, auto_init):
        self.path = path
        self
