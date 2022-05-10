import socket
from threading import Thread
import time



class ClientSocket(Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = 12312
        self.client.connect((self.host,self.port))
        self.parent = parent
        self.stop = False
        

    def run(self):
        print ("ClientSocket started")
        while not self.stop:
            self.data = self.client.recv(1024)

            if not self.data:
                continue

            else:
                self.parent.processing_incoming_message(self.data)
                pass

        print ("ClientSocket stopped")


    def kill(self):
        print ("killing ClientSocket")
        self.stop = True


    def send_message(self, message):
        self.client.send(message)

        
