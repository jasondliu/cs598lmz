import signal
# Test signal.setitimer() with SIGVTALRM.

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise SystemExit('Exiting')

signal.signal(signal.SIGVTALRM, handler)

# Schedule an alarm for 1 second.
signal.setitimer(signal.ITIMER_VIRTUAL, 1.0, 0)

# Busy-wait for a second.
now = time.time()
while time.time() < now + 2.0:
    pass

print('No alarm occurred')
