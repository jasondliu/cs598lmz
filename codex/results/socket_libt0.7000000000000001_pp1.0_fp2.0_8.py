import socket

class Client:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.socket.connect((self.host,self.port))
        except:
            self.socket.connect((self.host,self.port))

    def send(self,data):
        self.socket.send(data)

    def disconnect(self):
        self.socket.close()

def main():
    try:
        # Set up client
        client = Client('127.0.0.1',1337)
        client.connect()
        # Send data
        client.send(b'Hello')
        # Disconnect
        client.disconnect()

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
