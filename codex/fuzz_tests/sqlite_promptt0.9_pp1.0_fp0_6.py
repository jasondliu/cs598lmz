import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('dbname', uri,timeout=60.0). uri is a path (win) or host, ip, port pair.

## Establish the master socket
master_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
master_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
master_socket.bind(("",4896))
master_socket.listen(1)

## Establish the client socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client_socket.settimeout(60)
client_socket.connect(('localhost',4896))

## Establish the registrar socket and keep it open
registrar_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
registrar_socket.setsockopt(socket.SOL_SOCKET
