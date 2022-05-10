import select
import json
import time
import multiprocessing
import logging
import sys
import random

logging.basicConfig(level=logging.DEBUG,
                    filename='time_depth_pickle.log',
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


class PipeStream(object):
    def __init__(self, sock_addr, bufsize=1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(sock_addr)
        sock.listen(1)
        self.conn, self.addr = sock.accept()
        self.fd = self.conn.fileno()
        self.bufsize = bufsize
        self.buffer = b''
        self.closed = False

