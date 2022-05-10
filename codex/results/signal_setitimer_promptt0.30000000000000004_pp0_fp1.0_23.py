import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

signal.setitimer(signal.ITIMER_REAL, 0)
# Do some other work, and then allow the alarm (5 seconds)

print('do something...')
time.sleep(10)

print('do something...')
time.sleep(10)

print('do something...')
time.sleep(10)

print('do something...')
time.sleep(10)

print('do something...')
time.sleep(10)

print('do something...')
time.sleep(10)
