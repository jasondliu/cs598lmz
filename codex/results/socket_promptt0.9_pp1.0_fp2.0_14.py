import socket
# Test socket.if_indextoname
msg = socket.if_indextoname(1)
sys.stdout.write(msg)
