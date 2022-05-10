import socket
# Test socket.if_indextoname() with invalid index
try:
    r = socket.if_indextoname("1")
    print("try: socket.if_indextoname(\"1\"): " + r);
except socket.error as msg:
    print("except: socket.if_indextoname(\"1\"): " + msg);

# Test socket.if_indextoname() with valid index
try:
    r = socket.if_indextoname("2")
    print("try: socket.if_indextoname(\"2\"): " + r);
except socket.error as msg:
    print("except: socket.if_indextoname(\"2\"): " + msg);

# Test socket.if_indextoname() with invalid index
try:
    r = socket.if_indextoname("-1")
    print("try: socket.if_indextoname(\"-1\"): " + r);
except socket.error as msg:
    print("except: socket.if_indextoname(\"-1\"): " + msg);
