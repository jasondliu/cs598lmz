import socket
socket.if_indextoname('0')

my_ip = socket.gethostbyname(socket.gethostname())
print "My ip is:", my_ip

if my_ip[:3] == '192':
    print 'I am in the lab.'
elif my_ip[:3] == '10.':
    print 'I am at home.'
else:
    print 'I am somewhere else.'

s = socket.socket()
s.connect(('a.tcpip.biz', 80))
