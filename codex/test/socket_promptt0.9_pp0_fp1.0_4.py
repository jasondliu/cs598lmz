import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# >>>b'lo'

# >>b'en0'
print(socket.if_indextoname(0))

# >>>b'tun0'
print(socket.if_indextoname(2))

# >>>Traceback (most recent call last):
# >>>  ...
# >>>OSError: [Errno 19] No such device


# The None value is returned if the interface index is unknown.
if not socket.if_indextoname(300):
    print('Index is out of range')
# Index is out of range

# The None value is returned if the interface index is unknown.
if not socket.if_indextoname(300):
    print('Index is out of range')
# Index is out of range


from datetime import date

# Create function1 to accept a name
def function1(name):
    def function2():
        return "How are you %s" % name
    return function2

a = function1("Pyparang")
print(a())
