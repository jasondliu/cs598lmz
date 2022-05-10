import select
import socket
import sys
import threading
import time
import traceback

import six

try:
    import Queue as queue
except ImportError:
    import queue


def read_stream(stream, queue):
    while True:
        try:
            data = stream.read1(1024)
        except Exception as e:
            print('read error:', e)
            break
        if not data:
            print('read EOF')
            break
        queue.put(data)


def write_stream(stream, queue):
    while True:
        try:
            data = queue.get(True)
        except Exception as e:
            print('write error:', e)
            break
        try:
            stream.write(data)
        except Exception as e:
            print('write error:', e)
            break


class Server(object):
    def __init__(self, host, port, remote_host, remote_port, loop=None):
        self.host = host
        self.port = port
        self.remote_host = remote_
