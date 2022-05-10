import socket
# Test socket.if_indextoname

if __name__ == "__main__":
    print "Testing if_indextoname"
    ifindex = socket.if_nametoindex("lo")
    ifname = socket.if_indextoname(ifindex)
    if ifname != "lo":
        print "socket.if_indextoname(socket.if_nametoindex(\"lo\")) failed"
    else:
        print "Success"
