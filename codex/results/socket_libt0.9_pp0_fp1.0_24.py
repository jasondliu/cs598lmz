import socket
import struct
import sys

# Org 64 first bit for direction
# Initialize sender socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 50002

# Make a connection
client_socket.connect((HOST, PORT))

my_tuple = (1, "hello", 2.25)
my_data = pickle.dumps(my_tuple)
my_data_size = len(my_data)

# Need to send the size of the pickled data
data_packed_size = struct.pack("L", my_data_size)
client_socket.sendall(data_packed_size)

# Send the key
client_socket.sendall(my_data)
client_socket.close()
</code>
receiver.py
<code>#!/usr/bin/env python
import socket
import struct
import sys

# Discard the orginal 64 first bit for direction
# Initialize sender socket
client_socket = socket.socket(socket.
