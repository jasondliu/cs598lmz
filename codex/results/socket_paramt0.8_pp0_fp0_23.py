import socket
socket.if_indextoname(0)
socket.if_nametoindex("eth1")
socket.if_nametoindex("lo")
socket.if_nametoindex("eth0")

try:
    socket.if_nametoindex("")
except socket.error:
    pass

try:
    socket.if_nametoindex("z")
except socket.error:
    pass

try:
    socket.if_nametoindex("\0")
except socket.error:
    pass

try:
    socket.if_indextoname(1)
except socket.error:
    pass

# XXX: Assumes we have an interface called "lo" configured
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind(("", 9))
s.connect(("localhost", 9))
s.send("a")
socket.if_nametoindex("lo")
socket.if_indextoname(1)

################################################################################
# These tests require root privileges
################################################################################

if os.getuid() == 0:
