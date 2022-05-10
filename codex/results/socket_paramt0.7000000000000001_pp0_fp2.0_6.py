import socket
socket.if_indextoname(3)

#


import os, sys

cmd = 'ipconfig'

for line in os.popen(cmd).readlines():
    print line

print '\n'

print os.popen(cmd).read()

print '\n'

os.system(cmd)
