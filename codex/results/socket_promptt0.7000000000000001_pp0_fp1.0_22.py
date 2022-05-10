import socket
# Test socket.if_indextoname()
print "if_indextoname\t",
try:
    for i in range(0, 10):
        print socket.if_indextoname(i),
except socket.error as e:
    print e

# Test socket.if_nameindex()
print "\nif_nameindex\t\t",
try:
    for if_nameindex in socket.if_nameindex():
        print if_nameindex,
except socket.error as e:
    print e

# Test socket.if_nametoindex()
print "\nif_nametoindex\t",
try:
    for i in range(0, 10):
        print socket.if_nametoindex("t" + str(i)),
except socket.error as e:
    print e
