import socket
# Test socket.if_indextoname()

# AF_INET, AF_INET6
for af in [socket.AF_INET, socket.AF_INET6]:

    # Test with invalid index
    try:
        socket.if_indextoname(0, af)
    except socket.error as e:
        print("socket.if_indextoname(0, %s) failed: %s" % (af, e))

    # Test with valid index
    try:
        index = socket.if_nametoindex("lo")
        print("socket.if_nametoindex('lo') returned %d" % index)
        name = socket.if_indextoname(index, af)
        print("socket.if_indextoname(%d, %s) returned %s" % (index, af, name))
    except socket.error as e:
        print("socket.if_indextoname(socket.if_nametoindex('lo'), %s) failed: %s" % (af, e))
