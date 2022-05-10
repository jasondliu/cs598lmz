from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = decompress

import sys
import os

def main():
    argv = sys.argv[1:]
    if '-vv' in argv:
        fd_logger_level = logging.DEBUG
        argv.remove('-vv')
    else:
        fd_logger_level = logging.INFO
    if '-v' in argv:
        fd_logger_level = logging.WARNING
        argv.remove('-v')
    if '-h' in argv or '--help' in argv:
        print('Usage: %s [-v|-vv] [--fd-log-level <fd-log-level>] <config>' % sys.argv[0])
        return 0
    try:
        config_index = next(i for i, arg in enumerate(argv) if not arg.startswith('--'))
    except StopIteration:
        print('Usage: %s [-v|-vv] <config>' % sys.argv[0])
        return -1
    if '
