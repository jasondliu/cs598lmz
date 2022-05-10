import lzma
lzma.LZMAError

import multiprocessing
multiprocessing.cpu_count()

import os
os.EX_CANTCREAT

import pkg_resources
pkg_resources.require("foo")

import random
random.SystemRandom()

import re
re.compile(r'a')

import socket
socket.getservbyname("http")

import sqlite3
sqlite3.connect(":memory:")

import ssl
ssl.OPENSSL_VERSION

import sys
sys.getrefcount(None)

import termios
termios.tcgetattr(1)

import time
time.time()

import zlib
zlib.compressobj(9)

"""


def main():
    # Parse arguments.
    parser = argparse.ArgumentParser(
        description="Generate a list of builtin modules for a Python interpreter.")
    parser.add_argument("-p", "--python", default="python",
                        help="Path to the Python interpreter to use.")
    parser.add_argument("
