import signal
# Test signal.setitimer()

def handler(sig, frame):
    print('Got signal', sig)

signal.signal(signal.SIGALRM, handler)

print('Setting 1-second itimer')
signal.setitimer(signal.ITIMER_REAL, 1)
print('Sleeping')
time.sleep(5)
print('Done')
