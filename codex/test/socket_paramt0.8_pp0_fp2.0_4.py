import socket
socket.if_indextoname(interface)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  data, addr = s.recvfrom(10240)
  print(data)
