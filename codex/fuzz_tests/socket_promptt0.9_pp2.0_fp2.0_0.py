import socket
# Test socket.if_indextoname:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(1,10):
  try:
      print "%s - %s" % (i, socket.if_indextoname(i))
  except socket.error, e:
      print "%s - %s" % (i, e)

print socket.if_indextoname(16)
