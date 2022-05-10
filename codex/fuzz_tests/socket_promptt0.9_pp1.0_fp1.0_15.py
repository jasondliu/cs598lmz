import socket
# Test socket.if_indextoname()
print socket.if_indextoname(0)

# Test socket.if_nameindex()
print socket.if_nameindex()

# Test Issue #20059: a missing __hash__ in a tuple subclass could raise
# a TypeError instead of a TypeError.
try:
    hash(socket.if_nameindex())
except TypeError:
    pass

# Test issue #20645: if_nameindex can raise an OverflowError on 32-bit 
# Windows
try:
    namelist = socket.if_nameindex()
except OverflowError:
    pass
