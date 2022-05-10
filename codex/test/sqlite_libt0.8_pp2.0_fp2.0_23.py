import ctypes
import ctypes.util
import threading
import sqlite3
import signal
import getpass
import snowflake.client
import snowflake.connector
import snowflake.connector.errors
import snowflake.connector.converter

def call_with_retry(func, args=None, kwargs=None, retry_count=3):
    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}
    for retry_num in range(retry_count):
        try:
            return func(*args, **kwargs)
        except (Exception) as e:
            if retry_num == retry_count - 1:
                raise
            sleep_sec = 2 ** retry_num
            print(('fail to execute %s, try=%s, exception=%s, sleep=%s'
                % (func, retry_num, e, sleep_sec)))
            time.sleep(sleep_sec)

def to_json(obj):
    if not isinstance(obj, dict):
        obj = obj.__dict__
    return json.dumps
