import socket
# Test socket.if_indextoname()
if __name__ == '__main__':
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  print(s.if_indextoname(1))
