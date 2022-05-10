import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import os


# --------------------------- 
#  This class is for a single client
# ---------------------------

class ClientThread(threading.Thread):
    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] New thread started for "+ip+":"+str(port))
    
    def run(self):
        print("Connection from : "+ip+":"+str(port))
        self.clientsocket.send("Welcome to the server".encode())
        while 1:
            data = self.clientsocket.recv(2048)
            print("Client(%s:%s) sent : %s" % (self.ip, str(self.port), data))
            if (data == "exit"):
                break
        self.clientsocket.close()

# --------------------------- 
#  This class is for a server
# ------------------------
