import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    signal.setitimer(signal.ITIMER_REAL, 0.1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Do busy work
count = 0
while True:
    for i in range(10000):
        count += 1
</code>

