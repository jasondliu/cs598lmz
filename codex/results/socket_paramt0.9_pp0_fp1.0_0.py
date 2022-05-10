import socket
socket.if_indextoname(3)

#bind your client to a port for this example i binded my server to port 8000.
s.bind(('', 8000))
#you can bind the the port to a specific ip address, or to all interfaces, just like your server.
#s.bind(('10.10.10.100', 7000))

#listen to client packets
s.listen(1)
#receive the first message
conn, addr = s.accept()
#this is the main data loop.
while 1:
 #receive the data
  d = conn.recv(100)
  #if there is no data break out of loop.
  if not d: break
  #print the data to the console
  print d

#close socket
s.close()
