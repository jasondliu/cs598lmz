import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')


class DBService(threading.Thread):
    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.stop = False

    def run(self):
        # logging.info("%s start" % self.name)
        while not self.stop:
            try:
                data = self.sock.recv(1024)
                if data:
                    req = data.decode(encoding='utf-8').lower().split(" ")
                    cmd = req.pop(0)
                    if cmd == "get":
                        print("[DEBUG]", " ".join(req))
                        self.sock.send(self.handle_query(req))
                    elif cmd == "set":
                        print("[DEBUG]", " ".join(req))
                        self.sock.send(self.handle_insert(req).encode(
                            encoding='utf-8'))
                    elif cmd == "del":
                       
