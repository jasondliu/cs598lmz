import socket, sys, time
import os

# Set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(1)

# Print the port we're listening on
print "Listening on port %s" % s.getsockname()[1]

# Accept a connection
client, addr = s.accept()
print "Accepted connection from", addr

# Read the data
total_data=[]
while True:
    data = client.recv(16)
    if not data: break
    total_data.append(data)
    #print data,

# Close the connection
client.close()

file_name = total_data.pop(0)
print file_name

f = open(file_name, 'w')
f.write(''.join(total_data))
f.close()
