import socket
# Test socket.if_indextoname on a bogus interface index.
print(socket.if_indextoname(-1))
EOF
