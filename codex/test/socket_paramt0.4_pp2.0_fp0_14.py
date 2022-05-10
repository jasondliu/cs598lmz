import socket
socket.if_indextoname(3)

#%%
# Create a new socket for a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#%%
# Connect to a remote host
s.connect(('www.google.com', 80))

#%%
# Send data to the remote host
s.sendall(b'GET / HTTP/1.1\nHost: www.google.com\n\n')

#%%
# Receive data from the remote host
data = s.recv(1024)

#%%
# Close the connection
s.close()

#%%
# Print out the data that was received
print(data)

#%%
# Create a new socket for a UDP connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#%%
# Send data to the remote host
s.sendto(b'GET / HTTP/1.1\nHost: www.google.com\n\n', ('www.google.com', 80))

#%%
# Receive data
