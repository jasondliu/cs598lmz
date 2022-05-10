import socket
socket.if_indextoname(2)

# 'en0'

# https://stackoverflow.com/questions/12116685/how-can-i-get-my-machines-mac-address-in-python

# https://stackoverflow.com/questions/159137/getting-mac-address

import uuid

mac = uuid.getnode()

print(mac)

# https://stackoverflow.com/questions/28927958/python-get-mac-address

import uuid

mac = uuid.UUID(int = uuid.getnode()).hex[-12:]

print(mac)

# https://stackoverflow.com/questions/28927958/python-get-mac-address

import uuid

mac = uuid.UUID(int = uuid.getnode()).hex[-12:]

print(mac)

# https://stackoverflow.com/questions/28927958/python-get-mac-address

import uuid

mac = uuid.UUID(int = u
