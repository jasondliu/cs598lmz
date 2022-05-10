import socket
# Test socket.if_indextoname()
def getInterface(ifindex):
    """Return the name of an interface, given the index
The index is converted to an integer, if necessary"""
    return socket.if_indextoname(ifindex)

print "getInterface(2) =", getInterface(2)
print "getInterface('2') =", getInterface('2')
print

interfacenames = socket.if_nameindex()
print "We have interfaces:",
for index, name in interfacenames:
    print "  %d ==> %s" % (index, name)
print

# Test socket.if_nameindex()
def findAllInterfaces():
    """Return the list of interfaces"""
    interfaceNames = {}
    for index, name in socket.if_nameindex():
        interfaceNames[index] = name
    return interfaceNames

print "findAllInterfaces() =", findAllInterfaces()
print
