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

        while True:
            try:
                while True:
                    header = self.rfile.read(3)
                    if len(header) == 0:
                        raise IOError('client disconnected')
                    if header[0] != 0xff:
                        continue
                    break
                packet_id = header[1]

                length = header[2]
                for i in range(4):
                    data = self.rfile.read(1)
                    if len(data) == 0:
                        raise IOError('
