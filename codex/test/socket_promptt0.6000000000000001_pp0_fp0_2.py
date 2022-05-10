import socket
# Test socket.if_indextoname()
# https://docs.python.org/3/library/socket.html#socket.if_indextoname

def main():
  print(socket.if_indextoname(1))

if __name__ == "__main__":
  main()
