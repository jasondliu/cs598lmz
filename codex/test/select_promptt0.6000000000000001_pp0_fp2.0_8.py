import select
# Test select.select() with a list of sockets
import time
import threading
import socket
import sys

# Example of a threaded server that uses select()
# to handle multiple sockets at the same time.

# This server works on both IPv4 and IPv6.
# It is configured to listen on both protocols.
# Connect to it with IPv4 clients and IPv6 clients.

# This server is configured to accept connections
# from IPv6 clients, but not from IPv4 clients.
# Connect to it with IPv6 clients only.

# This server is configured to accept connections
# from IPv4 clients, but not from IPv6 clients.
# Connect to it with IPv4 clients only.

# This server is configured to accept connections
# from IPv4 clients and IPv6 clients.
# Connect to it with IPv4 clients and IPv6 clients.

HOST = '127.0.0.1'
PORT = 65432

# Get the address family of the host
# (AF_INET or AF_INET6).
# The host address is '' or 'localhost' or '127.0.0.1'.
# This server
