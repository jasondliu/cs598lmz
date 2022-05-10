import select
# Test select.select(), 1st parameter is list of socket descriptors for
# reading, 2nd parameter is list of socket descriptors for writing, 3rd parameter
# is list of socket descriptors for exceptions.

import threading
from time import sleep
from socket import socket, AF_INET, SOCK_STREAM

from framework import Test, TestFailed

from config import HOST, PORT, TIMEOUT

def lc(s):
    return s.lower()

def uc(s):
    return s.upper()


class select1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

    def run(self):
        global c
        global s
        global so1
        global so2
        global so3
        global so4
        global so5
        global so6
        global so7
        global so8

        while self.running:
            so1, so2, so3 = select.select([c], [], [], 0)
            so4, so5, so6
