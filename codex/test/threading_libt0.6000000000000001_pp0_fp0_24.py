import threading
threading.stack_size(67108864) # 64MB stack

class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):
        print("Connection de %s %s" % (self.ip, self.port, ))
        r = self.clientsocket.recv(2048)
        print("recu de %s %s" % (self.ip, self.port, ))
        print(r)
        self.clientsocket.send("5 / 5")
        print("envoye a %s %s" % (self.ip, self.port, ))
        self.clientsocket.close()

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tc
