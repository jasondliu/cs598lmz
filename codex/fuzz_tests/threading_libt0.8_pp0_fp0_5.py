import threading
threading.ThreadError

from socket import socket
import socket
socket.error
socket.timeout

try:
    print "try..."
    r = 10 / 0
    print "result", r
except ZeroDivisionError, e:
    print "except", e
finally:
    print "finally"
print "END"
