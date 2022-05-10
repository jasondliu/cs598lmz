import select
import pickle

#packet Objects
class Packet:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.size = 4096
        self.data = b''

    def receive(self):
        return self.conn.recv(self.size)

    def send(self, msg):
        self.conn.sendall(pickle.dumps(msg))

    def getAddr(self):
        return self.addr

    def getConn(self):
        return self.conn

    def close(self):
        self.conn.close()

#Server Object
class Server:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip, port))
        self.connections = []

    def startListening(self, numConnections=1):
        self.s.listen(numConnections)

    def acceptConnection(self):
        conn,
