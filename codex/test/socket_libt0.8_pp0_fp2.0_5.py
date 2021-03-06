import socket
import sys
import json

from mqtt_data_read import get_mqtt_data, mqtt_client, mqtt_topic

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
