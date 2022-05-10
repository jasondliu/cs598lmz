import socketserver
import threading

#Class for the server
class MyClientHandler(socketserver.BaseRequestHandler):
    #Method that handles the incoming message
    def handle(self):
        #Initiates a buffer to hold the amount of characters received
        self.data = self.request.recv(4096).strip()
        print("{} wrote:".format(self.client_address[0]))

        #Stores the data as a string
        msg = self.data.decode()

        #Closes the connection if variables are given
        if msg.lower() == "terminate":
            self.request.sendall(b'Terminated connection')
            print("Terminated connection")
            server.server_close()
            return

        #Prints the data that is sent, comma separated
        print(msg)

        #Sends the data back to the client
        self.request.sendall(self.data)

#Creates a server
class Server():
    def __init__(self, ip, port):
        #Creates a socketserver instance
        self.server =
