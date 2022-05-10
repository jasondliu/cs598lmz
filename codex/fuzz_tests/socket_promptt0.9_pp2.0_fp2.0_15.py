import socket
# Test socket.if_indextoname() by providing the result of
# socket.if_nametoindex() as the second argument.
# We don't care what the result is, we just care that the conversion
# doesn't crash on a -current Linux system.
socket.if_indextoname(0, b'\x00\x01\x02')
