import socket
socket.if_indextoname(17)

s = socket.socket()

s.bind(("", 5000))

s.listen(5)
c, addr = s.accept()
print 'Got a connection from', addr
c.send('Thank you for connecting')
c.close()
