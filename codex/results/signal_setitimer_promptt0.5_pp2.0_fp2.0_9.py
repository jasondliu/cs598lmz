import signal
# Test signal.setitimer

def handler(signum, frame):
    print('Got signal', signum)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

for i in range(100):
    print(i)
    time.sleep(1)

print('Done')
