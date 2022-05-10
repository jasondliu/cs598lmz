import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)
counter = 0
while True:
    counter += 1
    if counter > 8:
        signal.setitimer(signal.ITIMER_REAL, 0.5)
    print('test ', counter)
    time.sleep(1)
# End
