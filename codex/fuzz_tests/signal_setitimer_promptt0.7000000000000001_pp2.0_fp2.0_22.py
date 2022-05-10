import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1, 0.5)

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGALRM, handler)

for i in range(3):
    print('Sleeping', i)
    time.sleep(i)

print('Done')
