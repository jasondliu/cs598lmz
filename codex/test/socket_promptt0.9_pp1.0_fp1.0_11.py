import socket
# Test socket.if_indextoname() when an invalid index is passed.
#
# (1) On Darwin, the function raises a ValueError.
try:
  socket.if_indextoname(-1)
except ValueError as e:
  pass
else:
  raise Exception("-1 is an invalid index")
# (2) On Linux, the function instead returns None.
import sys
if sys.platform == "linux":
  v = socket.if_indextoname(-1)
  if v is not None:
    raise Exception("-1 is an invalid index")
