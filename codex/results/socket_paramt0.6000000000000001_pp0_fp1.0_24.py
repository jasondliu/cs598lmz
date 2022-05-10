import socket
socket.if_indextoname(34)

# create an inet, streaming socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80
# - the normal http port
s.connect(("www.python.org", 80))

# sendall function sends data to the socket.
s.sendall(b'GET / HTTP/1.0\r\n\r\n')

# the recv function reads data from the socket in chunks
# of 1024 bytes.
data = s.recv(1024)
# print out the first 1024 bytes of the response.
print(data)

# the rest of the response is the page.
while len(data) > 0:
    data = s.recv(1024)
    print(data)

# close the connection when done.
s.close()
