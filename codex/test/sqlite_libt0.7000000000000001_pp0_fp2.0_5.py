import ctypes
import ctypes.util
import threading
import sqlite3

def check_for_file(filename):
    if not os.path.isfile(filename):
        sys.exit('File %s does not exist.' % filename)

class HoneycombClient(object):

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((server_ip, server_port))

    def send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent


class Honeycomb(object):
    def __init__(self):
        self.honeycomb = ctypes.cdll.LoadLibrary(
            ctypes.util.find_library('honeycomb'))
