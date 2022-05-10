import signal
# Test signal.setitimer()


def handler(signum, frame):
    print "in handler"


signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.signal(signal.SIGALRM, handler)

# OUTPUT:
# Traceback (most recent call last):
#   File "signal/setitimer_2.py", line 14, in <module>
#     signal.signal(signal.SIGALRM, handler)
# ValueError: I/O operation on closed file
