import select
# Test select.select()
import socket
# Test IP and port
import sys
# Test sys.argv
import test_support
# Test threading module.
import threading
import time
# Test time.monotonic()
import unittest
import warnings

# Socket constants

TCP_PORT = 1234
UDP_PORT = 1234
HOST = '127.0.0.1'
HOSTv6 = '::1'

# For testing IP addresses
IPv4addr = "127.0.0.1"
IPv6addr = "::1"

IPV4_LOOPBACK = "127.0.0.1"
IPV6_LOOPBACK = "::1"

# Filenames used for tests

FNAME = "socket.dat"
FNAMEv6 = "socketv6.dat"

# When testing bind() and accept(), using numbered port addresses
# below 1024 (e.g. 80) can cause problems on systems with
# "privileged" ports.  So we use a port number (and create a server
# socket on that port)
