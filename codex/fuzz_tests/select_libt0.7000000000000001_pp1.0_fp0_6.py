import select
import socket
import threading
import time


class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.data = None

        self.sock = socket.socket()
        self.sock.bind(("", port))
        self.sock.listen(1)

        self.running = True
        self.start()

    def stop(self):
        self.running = False
        self.join()

    def run(self):
        while self.running == True:
            try:
                conn, addr = self.sock.accept()
                data = conn.recv(4096)

                self.data = data
                conn.close()
            except Exception, e:
                print e


class Talker(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port

        self.sock =
