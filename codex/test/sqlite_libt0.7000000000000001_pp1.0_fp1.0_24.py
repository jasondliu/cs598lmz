import ctypes
import ctypes.util
import threading
import sqlite3
import time

libc = ctypes.CDLL(ctypes.util.find_library('c'))

DEBUG_LOGGING = True

def debug(*args):
    if DEBUG_LOGGING:
        print(*args)

class ThreadedSocketServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ByteStreamHandler(socketserver.StreamRequestHandler):
    pass

class PacketHandler(ByteStreamHandler):
    def handle(self):
        conn = sqlite3.connect('static/example.db')

