import socket
import threading

HOST = "localhost"
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(100)

print "Listening on port {}".format(PORT)


class Client(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address

    def run(self):
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            else:
                print "Received {} bytes: {}".format(len(data), data)
                self.socket.send(data)

        self.socket.close()

while True:
    (client_socket, address) = s.accept()
    client_thread = Client((client_socket, address))
    client_thread.start()
