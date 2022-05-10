import io
# Test io.RawIOBase
io.RawIOBase
# Test io.BufferedIOBase
io.BufferedIOBase
# Test io.TextIOBase
io.TextIOBase

# Named tuple
from collections import namedtuple
namedtuple('_', ['foo', 'bar'])

# Sqlite
import sqlite3
sqlite3

# Imap
import imaplib
imaplib

# XML
import xml
xml

# ctypes
import ctypes
ctypes

# Parse/Compile
import py_compile

# Socket
import socket
socket.gethostbyname_ex
socket.socket
socket.socket.connect

# Socketserver
import socketserver
socketserver.ThreadingTCPServer
# Test the attribute on the class.
socketserver.ThreadingTCPServer.allow_reuse_address

# SSL
import ssl
ssl.wrap_socket

# Tarfile
import tarfile
tarfile.open('foo.tar')

# mmap
import mmap
mmap.mmap(-1, 0)

#
