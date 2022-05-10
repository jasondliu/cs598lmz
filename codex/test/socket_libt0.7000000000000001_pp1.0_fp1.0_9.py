import socket
import time

# Set the socket parameters
host = '192.168.0.2'
port = 5000

# Wait for the socket to connect
time.sleep (1)

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Send the data
msg = 'Hello world'

s.send(msg.encode())

# Close the socket
s.close()
