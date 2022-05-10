import socket

# Set up a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect as client to a selected server
# on a specified port
s.connect(("www.python.org", 80))

# Protocol exchange - sends and receives
s.sendall("GET /index.html HTTP/1.1\r\n\r\n")

reply = s.recv(1024) # Fill in start # Fill in end

# Print the reply
print(reply)
