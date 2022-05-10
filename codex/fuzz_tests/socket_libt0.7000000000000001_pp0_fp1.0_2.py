import socket
import sys

class Server:
    
    def __init__(self):
        self.HOST = socket.gethostname()
        self.PORT = 8888
        self.sckt = None
        self.conn = None
        self.addr = None
        
    def __del__(self):
        self.conn.close()
        self.sckt.close()
    
    def get_connection(self):
        return self.conn
    
    def open_connection(self):
        try:
            self.sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error as msg:
            print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
            sys.exit()
        try:
            self.sckt.bind((self.HOST,self.PORT))
        except socket.error as msg:
            print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg
