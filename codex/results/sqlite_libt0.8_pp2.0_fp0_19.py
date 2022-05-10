import ctypes
import ctypes.util
import threading
import sqlite3
import os
import atexit
import uuid
import contextlib
import time
import traceback
import logging

global api
global app_id
global res_id
global pkg_id
global sem
global library
global max_reopen
global reopen_counter
global max_history
global max_retries
global max_idle_time
global last_call
global __log__
global db_path
global db_conn
global db_cursor
global db_lock

application.log_format = '%(asctime)s %(module)s:%(lineno)d [%(levelname)s] %(message)s'

logger = logging.getLogger(__name__)
__log__ = logger

class TAPI_LOG_LEVEL:
    TAPI_LOG_NONE = 0
    TAPI_LOG_FATAL = 1
    TAPI_LOG_ERROR = 2
    TAPI_LOG_WARNING = 3
    TAPI_LOG_NOTICE = 4
    TAPI_LOG_TRACE = 5
    TAPI
