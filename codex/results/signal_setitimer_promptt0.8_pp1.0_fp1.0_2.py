import signal
# Test signal.setitimer()

def timeout_handler(signum, frame):
    print('Timeout #1\n')
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    print('Timeout #2\n')

# Callback 1
print('Connecting to server...\n')
signal.setitimer(signal.ITIMER_REAL, 2)
signal.signal(signal.SIGALRM, timeout_handler)

# Callback 2
#signal.pause()

while True:
    print('Wake Up')
    time.sleep(1)
