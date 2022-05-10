import socket
socket.if_indextoname(2)

# Enumerate the interfaces
for i in range(0, 10):
    try:
        print(socket.if_indextoname(i))
    except:
        pass

# Enumerate the interfaces
for i in range(0, 10):
    try:
        print(socket.if_indextoname(i))
    except OSError:
        pass

# Enumerate the interfaces
for i in range(0, 10):
    try:
        print(socket.if_indextoname(i))
    except OSError:
        pass
    except:
        pass

# Enumerate the interfaces
for i in range(0, 10):
    try:
        print(socket.if_indextoname(i))
    except OSError:
        pass
    except:
        pass
    else:
        pass

# Enumerate the interfaces
for i in range(0, 10):
    try:
        print(socket.if_indextoname(i))
    except OSError
