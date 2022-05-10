import socket
import time
import sys
import os

# Set up the host and port
host = 'localhost'
port = 8080

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((host, port))

# Receive the welcome message
welcome = s.recv(1024)
print welcome

# Send the username
s.send("USER test\r\n")

# Receive the response
response = s.recv(1024)
print response

# Send the password
s.send("PASS test\r\n")

# Receive the response
response = s.recv(1024)
print response

# Send the list command
s.send("LIST\r\n")

# Receive the response
response = s.recv(1024)
print response

# Send the quit command
s.send("QUIT\r\n")

# Close the connection
s.close()
