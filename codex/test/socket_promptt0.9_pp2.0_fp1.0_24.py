import socket
# Test socket.if_indextoname on missing interface, should raise IOError.
# The name ifinit_an.sh is used for parallelism in slow systems.
#
import socket
socket.if_indextoname(0xffffffff)
