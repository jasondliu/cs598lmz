import gc, weakref
from struct import unpack
from socket import inet_aton, inet_ntoa, ntohs, AF_INET, SOCK_STREAM, \
                  SOCK_DGRAM, socket, gethostbyname, gethostname, \
                  getaddrinfo, SHUT_RDWR
from time import sleep, time, localtime
from errno import EAGAIN, EINVAL, EINTR, ENETUNREACH, ECONNREFUSED, \
                    EHOSTUNREACH, EHOSTDOWN, ECONNRESET, ECONNABORTED, \
                    ENETDOWN, EADDRINUSE, ENOTCONN, ECONNREFUSED
from threading import Thread, Event
from os import name
from sys import version_info
from random import randint
from ctypes import windll
from collections import deque
from bisect import bisect
from itertools import count
from gevent.server import StreamServer
from gevent.socket import create_connection, error as socket_error, \
                          timeout as socket_timeout
from gevent.
