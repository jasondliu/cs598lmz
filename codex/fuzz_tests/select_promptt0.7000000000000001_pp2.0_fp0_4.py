import select
# Test select.select
select.select([],[],[])

import selectors
# Test the default selector
s = selectors.DefaultSelector()
s.close()

import shelve
# Test opening and closing a shelf
s = shelve.open(os.devnull)
s.close()

import socket
# Test socket.getaddrinfo
socket.getaddrinfo('127.0.0.1', 0)
socket.getaddrinfo('::1', 0)

# Test socket.getnameinfo
socket.getnameinfo(('127.0.0.1', 0), 0)
socket.getnameinfo(('::1', 0), 0)

# Test socket.getfqdn
socket.getfqdn('127.0.0.1')
socket.getfqdn('::1')

# Test socket.create_connection
socket.create_connection(('127.0.0.1', 0))
socket.create_connection(('::1', 0))

import sqlite3
# Test opening and closing a database
sqlite3.connect(':memory:')

import
