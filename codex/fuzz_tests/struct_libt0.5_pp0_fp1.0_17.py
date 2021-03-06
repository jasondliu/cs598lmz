import _struct
import ctypes
import errno
import fcntl
import os
import platform
import re
import select
import socket
import struct
import sys

from . import _common
from ._common import (
    AF_INET, AF_INET6, AF_UNSPEC, AI_ADDRCONFIG, AI_V4MAPPED,
    HAS_IPV6, HAS_SELECT, HAS_SELECT_POLL, HAS_SELECT_KQUEUE,
    HAS_SELECT_EPOLL, HAS_SELECT_DEVPOLL, HAS_SELECT_POLL_POLL,
    HAS_SELECT_POLL_EPOLL, HAS_SELECT_POLL_KQUEUE, HAS_SELECT_POLL_DEVPOLL,
    HAS_SELECT_POLL_COMPAT, HAS_SELECT_KQUEUE_POLL, HAS_SELECT_KQUEUE_EPOLL,
    HAS_SELECT_KQUEUE_KQUEUE, HAS_SELECT_KQUEUE_DEVPOLL,
    HAS_SELECT_KQUEUE_COM
