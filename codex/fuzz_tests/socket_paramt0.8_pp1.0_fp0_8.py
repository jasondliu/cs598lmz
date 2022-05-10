import socket
socket.if_indextoname(if_index)
socket.if_nameindex()
a = socket.if_nametoindex('eth0')
socket.if_nameindex()
a = socket.if_nametoindex('lo')
socket.if_nameindex()
socket.if_nametoindex('wlan0')

"""


"""
#for x in range(0,7):
#  print(x)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect((socket.gethostname(),1234))
#s.connect(('192.168.1.116',1234))
#s.connect(('192.168.1.112',1234))
#s.connect(('192.168.1.109',1234))
#s.connect(('192.168.1.101',1234))
#while True:
#    full_msg = ''
#    while True:
#        msg = s.recv(8)
#        if len(msg) <= 0:
#            break
#        full_msg += msg
