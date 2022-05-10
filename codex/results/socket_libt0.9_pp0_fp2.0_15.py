import socket
import threading

#
# Print a nice banner with information on which port we're listening.
#

print "Locking server" + \
         " up on port %s" % (5600)

#
# Create a TCP/IP socket
#

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#
# Bind the socket to the port
#

serversocket.bind(('localhost', 5600))

#
# Listen for incoming connections
#
serversocket.listen(5)

#
# Function to handle client in a new thread.
#
def clienHandler(clientsocket, addr):
    while True:
    
        #
        # Receiving from client
        #
        
        data = clientsocket.recv(1024)
        
        print "Data: [" + data + "]"
        
        #
        # Send data to the client
        #

        if data:
            datalist = data.split()
            command = datalist[0]
            print "command %
