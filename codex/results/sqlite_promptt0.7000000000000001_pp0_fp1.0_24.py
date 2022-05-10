import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import json
import time
import sys

if sys.platform == 'win32':
    import msvcrt
else:
    import atexit
    import os

# http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
import datetime

# set the path to the library
if sys.platform == 'win32':
    libcrypto = ctypes.cdll.LoadLibrary('./libcrypto.dll')
else:
    libcrypto = ctypes.cdll.LoadLibrary('./libcrypto.so')

def parse_dict_to_parsed_json(dict_to_parse):
    """
    This function parses a dict to a stringified JSON
    """
    return json.dumps(dict_to_parse)

def parse_dict_to_json(dict_to_parse):
    """
    This function parses a dict to a stringified JSON
    """
    return json.dumps(dict_to_parse)


