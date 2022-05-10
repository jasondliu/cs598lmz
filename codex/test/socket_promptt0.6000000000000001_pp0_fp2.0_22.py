import socket
# Test socket.if_indextoname(), socket.if_nametoindex(), and
# socket.getnameinfo() with a large number of interfaces.
import os
import sys
import socket
import unittest
import test.support
import test.support.threading_helper
import threading
import time
import warnings
import weakref
warnings.filterwarnings('ignore', '.*socket.getnameinfo.*',
    DeprecationWarning, __name__)
SIOCGIFNAME = 0x8910
SIOCGIFINDEX = 0x8933
SIOCGIFCONF = 0x8912
SIOCGIFFLAGS = 0x8913
IFF_UP = 0x1
IFF_LOOPBACK = 0x8
IFF_RUNNING = 0x40
IFF_MULTICAST = 0x1000
IFF_BROADCAST = 0x2
IFF_POINTOPOINT = 0x10
IFF_LOOPBACK = 0x8
IFF_NOARP = 0x80
IFF_SLAVE = 0x800
IFF_MASTER = 0x400
