import socket
# Test socket.if_indextoname() with invalid arguments
for i in (-1, 0):
    try:
        socket.if_indextoname(i)
    except TypeError:
        pass
    except ValueError:
        pass
    except socket.error:
        pass
