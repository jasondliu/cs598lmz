import select
# Test select.select double-closed fd
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.google.com', 80))
s.close()
# XXX: the result is different because we did not close the fd 2
# (stderr). To yield the same result we close the fd 2 case by case
# with this code
# def test(x):
#     print x
#     select.select([x], [], [])
#
# test(2)
try:
    select.select([s], [], [])
except Exception as e:
    print e
    print "OK"
# XXX: OSError: [Errno 9] Bad file descriptor
# OK

# Test select.select double-closed fd
try:
    select.select([s], [], [])
except Exception as e:
    print e
    print "OK"
# XXX: OSError: [Errno 9] Bad file descriptor
# OK

# Another test with a socket
s = socket.
