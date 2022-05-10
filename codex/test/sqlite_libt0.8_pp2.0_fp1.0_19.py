import ctypes
import ctypes.util
import threading
import sqlite3
from . import _sqlite3

def convert_timestamp(timestamp):
    """Convert a unix timestamp (seconds since 1970) to a datetime object."""

    if timestamp is None:
        return None
    return datetime.fromtimestamp(timestamp)

def convert_timedelta(interval):
    """Convert a time interval in milliseconds to a timedelta object."""

    if interval is None:
        return None
    return timedelta(milliseconds=interval)

def convert_date(date):
    """Convert a Julian day number to a date object."""

    if date is None:
        return None
    return datetime.fromordinal(date - 2440587.5)

def convert_storage_size(size):
    """Convert a storage size in bytes to a string."""

    if size is None:
        return None
    if size >= 1024*1024*1024:
        return '{} GiB'.format(size // (1024*1024*1024))
