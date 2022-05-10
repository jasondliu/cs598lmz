import ctypes
import ctypes.util
import threading
import sqlite3
from bottle import route, run
import logging
from logging.handlers import RotatingFileHandler
from config import *
import json


# Handle non-exception error codes (which may still include an error msg).
def check_status(status, func, args):
    if status == 1:
        logger.info('Transaction validated (by %s).' % (args[0]))
    elif status == -1:
        logger.error('Transaction invalid (by %s).' % (args[0]))
    elif status == -2:
        logger.error('Transaction rejected by %s.' % (args[0]))
    elif status == -3:
        logger.warning('Transaction ignored by %s.' % (args[0]))
    elif status == -5:
        logger.error('Transaction failed to apply (by %s).' % (args[0]))
    elif status == -6:
        logger.error('Transaction rejected as invalid by %s.' % (args[0]))
