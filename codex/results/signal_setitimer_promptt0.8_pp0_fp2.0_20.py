import signal
# Test signal.setitimer
def handler(sig, frame):
    print('Signal handler called with signal', sig)
    raise OSError("Couldn't open device!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0) # seconds

d = d2xx.open(0)

# Test cancellation
d = d2xx.open(3)
assert d.isOpen() == 0

# Test close
d = d2xx.open(0)
assert d.isOpen() == 1
d.close()
assert d.isOpen() == 0

print('all tests succeeded')
