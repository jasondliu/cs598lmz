import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging

#TODO put in config file
import config

def main():
    try:
        mainloop(sys.argv[1:])
    except KeyboardInterrupt:
        os._exit(0)


def mainloop(argv):
    loglevel = loglevel_string_to_int(config.LogLevel)
    nfcpy_logger = logging.getLogger('nfc')
    nfcpy_logger.setLevel(logging.ERROR)

    logging.basicConfig(level=loglevel,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

