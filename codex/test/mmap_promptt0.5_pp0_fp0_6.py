import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)

import os
# Test os.open("/dev/null", os.O_RDONLY)

import py_compile
# Test py_compile.compile("/dev/null", doraise=True)

import random
# Test random.seed()

import readline
# Test readline.parse_and_bind("")

import select
# Test select.select([], [], [], 0)

import socket
# Test socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("localhost", 80))

import sqlite3
# Test sqlite3.connect("/dev/null")

import ssl
# Test ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
#                     ssl_version=ssl.PROTOCOL_TLSv1)

import subprocess
# Test subprocess.Popen(["ls"], stdout=subprocess.PIPE)
