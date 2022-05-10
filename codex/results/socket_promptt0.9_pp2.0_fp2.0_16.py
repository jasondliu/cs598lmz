import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)
var = socket.if_indextoname(1)
if var:
  print var
else:
  print "var does not have a value"
# Test socket.if_index
index = socket.if_index(var)
if index:
  print index
else:
  print "index does not have a value"
# Test socket.if_nameindex
try:
  list_of_interfaces = socket.if_nameindex()
except socket.error:
  print "Invalid Argument or bad results from if_nameindex"
else:
  print "Got list of interfaces"
  cnt = 0
  while list_of_interfaces[cnt]:
    print ("Interface[%s] name == %r, index == %s" %
          (cnt, list_of_interfaces[cnt][1], list_of_interfaces[cnt][0]))
    cnt += 1
# Test socket.ntohl/socket.htonl
# Use the address of one of our things
my_net =
