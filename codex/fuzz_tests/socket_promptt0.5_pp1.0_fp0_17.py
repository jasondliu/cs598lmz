import socket
# Test socket.if_indextoname()

def try_if_indextoname(index):
    try:
        return socket.if_indextoname(index)
    except:
        return None

print('Testing socket.if_indextoname()')
print('if_indextoname(0) =', try_if_indextoname(0))
print('if_indextoname(1) =', try_if_indextoname(1))
print('if_indextoname(2) =', try_if_indextoname(2))
print('if_indextoname(3) =', try_if_indextoname(3))
print('if_indextoname(4) =', try_if_indextoname(4))
print('if_indextoname(5) =', try_if_indextoname(5))
print('if_indextoname(6) =', try_if_indextoname(6))
print('if_indextoname(7) =', try_if_indextoname(7
