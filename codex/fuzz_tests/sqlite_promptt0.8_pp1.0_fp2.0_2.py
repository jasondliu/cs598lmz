import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

from sqlite_test import dbapi2

from sqlite3 import apsw

from sqlite_test import test_ttt
from sqlite_test.test_ttt import test_ttt

from sqlite_test import test_ttt_py
from sqlite_test.test_ttt_py import test_ttt_py



def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        # Setup the command line arguments.
        parser = ArgumentParser(
            description="""\
                  """,
            epilog="""""")
        parser.add_argument("-c", "--config",
                          dest="config", default='./config.ini',
                          help="use a config file", metavar="FILE")
        parser.add_argument("-n", "--noninteractive",
                          dest="noninteractive", action='store_true',
                          help="don't ask for user input")
        parser.add_argument("-e", "--err",
