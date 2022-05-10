import threading
threading.stack_size(2**27)

class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('', 80))
        while True:
            try:
                data, addr = self.s.recvfrom(200)
                self.s.sendto('HTTP/1.1 200 OK\nConnection: close\nContent-Length: 0\n\n'.encode('utf-8'), addr)
            except Exception:
                pass

Server()

import os
os.system('sudo cp udpserver.py /home/pi/')
os.system('sudo /home/pi/udpserver.py &')
