import socket
socket.if_indextoname(1)

# get the local ip
print (socket.gethostbyname_ex(socket.gethostname()))

# get the MAC address
import uuid
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

# get the MAC address
import uuid
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

# get the python version
import sys
print (sys.version)

# get the python version
import platform
print (platform.python_version())

# get the python version
import sys
print (sys.version)

# get the python version
import platform
print (platform.python_version())

# get the python version
import sys
print (sys.version)

# get the python version
import platform
print (platform.python_version
