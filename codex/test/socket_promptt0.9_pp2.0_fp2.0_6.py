import socket
# Test socket.if_indextoname
try: socket.if_indextoname(999)
except socket.error: pass
else: fail("socket.if_indextoname(999) should fail")
# Some platforms may have an alias
if socket.if_indextoname(socket.if_nametoindex("lo")) != "lo":
    raise TestFailed("socket.if_indextoname(socket.if_nametoindex('lo')) "
                     "returned wrong result")
if socket.if_indextoname(socket.if_nametoindex("lo0")) != "lo0":
    raise TestFailed("socket.if_indextoname(socket.if_nametoindex('lo0')) "
                     "returned wrong result")
# Test socket.if_nameindex
try: socket.if_nameindex()
except socket.error: pass
else: fail("socket.if_nameindex() should fail")
# Test socket.if_nametoindex
try: socket.if_nametoindex('')
except socket.error: pass
