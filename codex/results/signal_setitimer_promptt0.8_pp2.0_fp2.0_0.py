import signal
# Test signal.setitimer for SIGVTALRM
def _sigvtalrm_handler(signum, frame):
    print('SIGVTALRM handler called')

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGVTALRM, _sigvtalrm_handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/pts/2', os.O_RDWR)
os.close(fd)
