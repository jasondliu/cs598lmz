import mmap
import operator
import os
import re
import socket
import struct
import sys
import time

from config import config
import dnsdist_parser
import dnsdist_stats
import dnsdist_test
import redis_db
import utils

# the regex used to parse dnsdist configuration files
section_regex = re.compile(r'^--\s+(\S+)\s+--$')
config_regex = re.compile(r'^\s*(\S+)\s*=\s*(\S+)$')

def get_stats_socket():
    filename = config.get('dnsdist', 'stats_socket')
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(filename)
    return sock

def reset_stats(stats_socket):
    stats_socket.sendall('forgetCounters()\n')

def read_stats(stats_socket):
    stats_socket.sendall('getAll()\n')
    data = stats_socket.recv
