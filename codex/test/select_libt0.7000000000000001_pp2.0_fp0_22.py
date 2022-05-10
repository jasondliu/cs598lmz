import select
import socket
import sys

from . import dispatcher
from .addr import ADDR, ADDR_TYPE
from . import dns_resolver
from . import socks5
from . import tcprelay
from . import udprelay
from . import common
from . import eventloop
from . import shell


def is_local(addr):
    host, port = addr
    if host == '127.0.0.1' or host == 'localhost':
        return True
    return False


def is_valid_port(port):
    try:
        port = int(port)
    except ValueError:
        return False
    if port <= 0 or port > 65535:
        return False
    return True


def parse_header(data):
    header_length = ord(data[0])
    return data[1:header_length+1], data[header_length+1:]


def parse_dest(data):
    addrtype = ord(data[0])
    dest_addr = None
    dest_port = None
