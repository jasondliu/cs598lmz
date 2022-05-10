import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)

import os
# Test os.ftruncate(0, 0)

import pty
# Test pty.fork()

import resource
# Test resource.getrlimit(resource.RLIMIT_NOFILE)

import select
# Test select.select([], [], [], 0)

import signal
# Test signal.signal(signal.SIGCHLD, signal.SIG_DFL)

import socket
# Test socket.socketpair()

import termios
# Test termios.tcgetattr(0)

import thread
# Test thread.start_new_thread(lambda: None, ())

import threading
# Test threading.Thread(target=lambda: None).start()

import time
# Test time.sleep(0)

import tty
# Test tty.setraw(0)

import unicodedata
# Test unicodedata.normalize('NFD', u'\u1e9b\u0323')

import zip
