import socket
# Test socket.if_indextoname(), socket.if_nameindex()
if_nameindex = socket.if_nameindex()
for i, name in if_nameindex:
    print '%s: %s' % (i, name)
    try:
        i, name = if_indextoname(i)
        print name
    except OSError:
        try:
            i, name = if_indextoname(i-1)
            print name
        except OSError:
            try:
                i, name = if_indextoname(i-1)
                print name
            except OSError:
                i, name = if_indextoname(i-1)
                print name

# Test socket.if_nametoindex()
for i, name in if_nameindex:
    print '%s: %s' % (i, name)
    try:
        index = if_nametoindex(name)
    except OSError:
        pass

if_nameindex = socket.if_nameindex()
for i,name in if_name
