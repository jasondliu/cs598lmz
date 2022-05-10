import select
import random
import sys
import time
import socket
import os
import logging
import threading


class Server:
    def __init__(self, port, timeout, logfile):
        self.port = port
        self.timeout = timeout
        self.logfile = logfile
        self.logger = logging.getLogger('server')
        self.__init_logger()

    def __init_logger(self):
        logging.basicConfig(
            filename=self.logfile,
            level=logging.DEBUG,
            format='%(asctime)s %(message)s',
            datefmt='%Y.%m.%d %I:%M:%S')
        # print to console too
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

