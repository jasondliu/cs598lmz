import socket
# Test socket.if_indextoname()                      
ifname = socket.if_indextoname(1)

if ifname:
    print(ifname)
else:
    print('Not found')

# Test various socket errors.

try:
    socket.socket(-1, socket.SOCK_STREAM)
except socket.error as msg:
    print('SKIP')
    sys.exit()

s = socket.socket()

# An invalid socket must raise
# an error when calling setsockopt
try:
    s.setsockopt(1, socket.SO_ACCEPTCONN, 1)
except socket.error as msg:
    # Either ENOTSOCK (19) or ENOPROTOOPT (92)
    # (E.g. OS X uses 92)
    if msg.args[0] not in (19, 92):
        print('Unexpected error:', msg)
    print('ok')

# An invalid socket must raise
# an error when calling getsockopt
try:
    s.getsockopt(1, socket.SO_ACCEPTCONN
