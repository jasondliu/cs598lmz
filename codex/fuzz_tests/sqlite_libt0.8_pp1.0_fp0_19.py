import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import atexit
import os


def _sqlite3_retry(f):
    def retry_func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except sqlite3.OperationalError as e:
            if hasattr(e, 'message') and (e.message == 'database is locked' or e.message == 'database is locked. '):
                time.sleep(0.001)
                return retry_func(*args, **kwargs)
            else:
                raise

    return retry_func


class Blocklist(object):
    def __init__(self, data_dir, sql_db_name, blocklist_url):
        self.data_dir = data_dir
        self.sql_db_name = sql_db_name
        self.blocklist_url = blocklist_url

    @staticmethod
    def _add_host(host):
        lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('bloomd'))
        lib.
