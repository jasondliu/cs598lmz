import socket
socket.if_indextoname(1)

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print 'afinet'
except socket.error,e:
    print 'af-unix'

print (socket.socket(socket.AF_INET,socket.SOCK_STREAM))
print (socket.socket(socket.AF_UNIX,socket.SOCK_STREAM))

print (socket.SO_REUSEADDR)
print (socket.SOL_SOCKET)
print (socket.SO_TYPE)
print (socket.SO_ERROR)

print (socket.SOMAXCONN)
print (socket.SOL_SOCKET)
print (socket.MSG_PEEK)
print (socket.MSG_WAITALL)
print (socket.MSG_OOB)

print (socket.AI_PASSIVE)
print (socket.AI_CANONNAME)

print (socket.AF_INET)
print (socket.AF_UNIX)

print (socket.SOCK_DGRAM
