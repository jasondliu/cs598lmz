import select
import sys
import time
import traceback

try:
    import json
except ImportError:
    import simplejson as json

from gntp.error import NetworkError


__all__ = ['GrowlNotifier']


_debug = os.environ.get('GNTP_DEBUG', False)


def _write_data(sock, data):
    bytes_sent = 0
    while bytes_sent < len(data):
        bytes_sent += sock.send(data[bytes_sent:])


def _read_data(sock, size):
    bytes_read = 0
    data = ''
    while bytes_read < size:
        data += sock.recv(size - bytes_read)
        bytes_read = len(data)

    return data


def _read_line(sock):
    line = ''
    while not line or line[-1] != '\n':
        line += sock.recv(1)

    return line
