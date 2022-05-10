import socket
# Test socket.if_indextoname
# http://bugs.python.org/issue11821
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.bind(('::1', 0))
indices = set(s.getsockopt(socket.SOL_SOCKET,
                           socket.SO_BINDTODEVICE, 16)
              .decode('latin-1').split(','))
for index in indices:
    socket.if_indextoname(int(index))

# Test s.recvmsg() method.
# http://bugs.python.org/issue15792
recvmsg_test_repeat = 100
msg_type = 0
msg_pid = 0

def recvmsg_setup():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 0))
