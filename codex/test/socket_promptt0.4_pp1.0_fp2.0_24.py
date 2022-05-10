import socket
# Test socket.if_indextoname()
# https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
print(socket.if_indextoname(1))

# Test socket.gethostname()
# https://stackoverflow.com/questions/4271740/how-to-get-the-current-computers-name-in-python
print(socket.gethostname())

# Test socket.gethostbyname()
# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
print(socket.gethostbyname(socket.gethostname()))

# Test socket.gethostbyname_ex()
# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
print(socket.gethostbyname_ex(socket.gethostname()))

# Test socket.gethostbyaddr()
# https://stackoverflow.
