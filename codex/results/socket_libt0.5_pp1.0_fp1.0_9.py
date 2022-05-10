import socket
import time
import threading

class UDP_Server(threading.Thread):
    def __init__(self, port, addr):
        threading.Thread.__init__(self)
        self.port = port
        self.addr = addr
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.addr, self.port))
        self.sock.settimeout(1)
        self.data = ''
        self.run_flag = True

    def run(self):
        print('Server thread started')
        while self.run_flag:
            try:
                self.data, self.addr = self.sock.recvfrom(1024)
                print('Got data: %s' % self.data)
            except socket.timeout:
                pass

    def stop(self):
        self.run_flag = False
        self.sock.close()


class UDP_Client(threading.Thread):
    def __init__(self, port, addr):
