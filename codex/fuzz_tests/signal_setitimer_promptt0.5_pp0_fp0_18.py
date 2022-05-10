import signal
# Test signal.setitimer

def handler(sig, frame):
    print 'Received', sig, frame

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

print 'Done'
