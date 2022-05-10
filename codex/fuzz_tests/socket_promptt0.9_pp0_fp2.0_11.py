import socket
# Test socket.if_indextoname

print(socket.if_indextoname(0))
print(socket.if_indextoname(1))
print(socket.if_indextoname(100))
#Test socket.if_nameindex
print(socket.if_nameindex())
#Test socket.if_nametoindex
print(socket.if_nametoindex("en0"))
#Test socket.setdefaulttimeout
try:
    socket.setdefaulttimeout(99.0)
except (OSError, TypeError) as e:
    print ("Caught exception invoking socket.setdefaulttimeout: %s" % e)
    try:
        socket.setdefaulttimeout('hund')
    except (OSError, TypeError) as e:
        print ("Caught exception invoking socket.setdefaulttimeout: %s" % e)
        try:
            socket.setdefaulttimeout(None)
        except AttributeError as e:
            print ("Caught exception invoking socket.setdefaulttimeout: %s" % e)
