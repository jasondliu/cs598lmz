import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(1))
print(socket.if_indextoname(1, 0))
try:
    print(socket.if_indextoname(-1))
except ValueError:
    print("ValueError")

# Test socket.gethostname
print(socket.gethostname())
# Test socket.gethostbyname
print(socket.gethostbyname("localhost"))
print(socket.gethostbyname("127.0.0.1"))
print(socket.gethostbyname(""))
print(socket.gethostbyname(""))
print(socket.gethostbyname("1234"))
print(socket.gethostbyname(""))
# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("localhost"))
print(socket.gethostbyname_ex(""))
print(socket.gethostbyname_ex(""))
print(socket.gethostbyname_ex(""))
print(socket.
