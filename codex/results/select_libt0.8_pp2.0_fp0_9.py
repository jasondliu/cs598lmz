import select

PORT = 8091
HOST = "127.0.0.1"

class Client:
        def __init__(self,host,port):
                self.host = HOST
                self.port = PORT
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                        self.socket.connect((host, port))
                        print "\n- Server Connection Established -\n"
                except Exception, e:
                        print e
                        print "\n\n- Server Connection Error -\n\n"
        def UserInput(self):
                while True:
                        msg = raw_input(">>")
                        self.socket.send(msg)

Client(HOST,PORT)
