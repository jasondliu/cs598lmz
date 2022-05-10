import socket
# Test socket.if_indextoname(3, '16')
m = socket.if_indextoname(3, 16)
print(m)

# Test socket.if_indextoname(3, '16') with wrong arguments - ValueError
try:
  a = socket.if_indextoname(3, 16, 1)
except ValueError as e:
  print(e)

# Test socket.if_indextoname(3, '16') with wrong arguments - TypeError
try:
  b = socket.if_indextoname('3', 16)
except TypeError as e:
  print(e)

# Test socket.if_indextoname(3, '16') with wrong arguments - OSError
try:
  c = socket.if_indextoname(4, 16)
except OSError as e:
  print(e)

try:
  d = socket.if_indextoname(3, 17)
except OSError as e:
  print(e)

# Test socket.if_indextoname(3,
