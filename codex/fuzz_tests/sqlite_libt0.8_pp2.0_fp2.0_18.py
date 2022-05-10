import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import subprocess


# Global constants.
XMPY_CHECK_INTERVAL = 10
XMPY_MIN_JOBS = 5
XMPY_MAX_JOBS = 20
XMPY_MAX_RETRIES = 3
XMPY_DB = '~/xmpy_jobs.db'
XMPY_SESSION_ID = os.getenv('XMPY_SESSION_ID', 'localhost')


# GLOBAL VARIABLES
XMPY_STOP_RUNNING = False


def db_print(sql):
    try:
        conn = sqlite3.connect(os.path.expanduser(XMPY_DB))
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        conn.close()
    except:
        print('Failed to execute SQL: {0}'.format(sql))


def get_current_jobs(session_id=XMPY_SESSION_ID):
    """
    Return all the jobs in the database that are currently
