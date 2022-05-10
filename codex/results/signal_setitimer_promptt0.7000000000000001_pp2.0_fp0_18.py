import signal
# Test signal.setitimer()

def handler(sig, frame):
    print "Catch signal=%s, frame=%s" % (sig, frame)

signal.signal(signal.SIGALRM, handler)

print "Set timer..."
signal.setitimer(signal.ITIMER_REAL, 3, 0)
print "Set timer done."

# Wait the signal
while True:
    pass
