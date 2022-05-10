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
    if name != ifname:
      print "[%d] %s" % (ifindex, name)
  return name

def test_if_nametoindex():
  test_if_indextoname()
  ifname = name
  ifindex = if_nametoindex(ifname)
  print "if_nametoindex(%s) = %d" % (ifname, ifindex)
  return ifindex

def test_socket_type():
  # Test SOCK_DGRAM
  print "SOCK_DGRAM = %d" % SOCK_DGRAM
  # Test SOCK
