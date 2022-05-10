import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Call handler() on SIGALRM
signal.signal(signal.SIGALRM, handler)

# Schedule the first alarm for 1 second from now
signal.setitimer(signal.ITIMER_REAL, 1)

# Busy loop for 5 seconds
while True:
    print('Busy looping ...')
    time.sleep(0.25)

# Schedule the next alarm for 2 seconds from now
signal.setitimer(signal.ITIMER_REAL, 2)

# Busy loop for 5 seconds
while True:
    print('Busy looping ...')
    time.sleep(0.25)

# Schedule the next alarm for 3 seconds from now
signal.setitimer(signal.ITIMER_REAL, 3)

# Busy loop for 5 seconds
while True:
    print('Busy looping ...')
    time.sleep(0.25)

# Schedule the next alarm for 4
