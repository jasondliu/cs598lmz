import threading
threading.stack_size(1024*1024)

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind to port
server_address = ('', 10000)
s.bind(server_address)

#listen to socket and wait for connection
s.listen(5)
#print 'Server is listening'

#accept the connection
conn, addr = s.accept()
#print conn

#send data to client
data = 'This is server.'
conn.send(data.encode())
