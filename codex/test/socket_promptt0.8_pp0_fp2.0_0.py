import socket
# Test socket.if_indextoname()

SOCK_DGRAM = socket.SOCK_DGRAM
SOCK_STREAM = socket.SOCK_STREAM

if_indextoname = socket.if_indextoname
if_nametoindex = socket.if_nametoindex

def test_if_indextoname():
  for ifindex in range(0, 5):
    name = if_indextoname(ifindex)
    ifname = ifindex
