import socket
import threading

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_msg = ""
    
    
    def __init__(self, address):
        self.sock.connect((address, 12345))
        
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))
        
    def sendMsg(self):
        while True:
            self.send_msg = input()
            self.sock.send(bytes(self.send_msg, 'utf-8'))
        
if __name__ == '__main__':
    client = Client("127.0.0.1")

#SocketServer
import socketserver
import threading

def clientthread(conn):
    while True:
        data = conn.rec
