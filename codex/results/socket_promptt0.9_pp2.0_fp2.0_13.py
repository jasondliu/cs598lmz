import socket
# Test socket.if_indextoname(), a function new in Python 3.3

# Test if_indextoname()
# Try to find the right parameter for if_indextoname()
# Note: This test works because it is executed by a testrunner that
#       detects all network interfaces at the beginning of a run.
#
for i in range(256):
    try:
        if_indextoname(i)
        if i > 1:
            raise TestFailed(i)
    except OSError:
        if i < 2:
            raise TestFailed(i)
#
# Test if_indextoname()
# A bad parameter to if_indextoname() should raise an OSError (if it is not)
# a real exception of the OS.
#
try:
    if_indextoname('1')
except TypeError:
    pass
except OSError:
    pass
else:
    raise TestFailed('TypeError expected')
try:
    if_indextoname(-1)
except ValueError:
    pass
except OSError:
