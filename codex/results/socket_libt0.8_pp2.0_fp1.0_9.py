import socket
import sys
import threading
import time
import Util
import Neighbor

class Client(threading.Thread):

    #constructor
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.port = port
        self.host = host
        self.clientSocket = None
        self.bufferSize = 1024
        self.start()

    #thread's main loop
    def run(self):
        while True:
            try:
                #open socket
                self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.clientSocket.connect((self.host, self.port))

                #start sender and receiver threads
                SenderThread(self.clientSocket).start()
                ReceiverThread(self.clientSocket).start()
            except:
                print("Sleeping for 1 minute before trying to reconnect to server: ")
                time
