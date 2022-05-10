import _struct
import logging
import os
import random
import socket
import struct
import sys
import time
import traceback

import numpy as np

if sys.argv[0] != 'python':
    # if the process isn't called python, assume that the script is being run
    # from the command line
    import argparse

    parser = argparse.ArgumentParser(description='Run a client to test the server')
    parser.add_argument('-s', '--server', dest='server', default='localhost', help='the server to connect to')
    parser.add_argument('-p', '--port', dest='port', default=9876, help='the port to connect to')
    parser.add_argument('-c', '--command', dest='command', default='', help='the command to send')
    parser.add_argument('-b', '--buffer-size', dest='buffer_size', default=1024, help='the buffer size to send')
    parser.add_argument('-d', '--delay', dest='delay', default=0.0, help='the delay between commands
