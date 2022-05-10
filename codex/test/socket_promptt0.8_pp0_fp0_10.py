import socket
# Test socket.if_indextoname()
try:
  print(socket.if_indextoname(1))
except ValueError:
  # No route to index
  pass

# Test socket.if_nametoindex()
try:
  print(socket.if_nametoindex('lo'))
except ValueError:
  # No interface with name
  pass
