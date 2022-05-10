import signal
# Test signal.setitimer()

def handler(signum, frame):
    print('Signal handler called with signal', signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,5)

# This open() may hang indefinitely
fd = os.open('/dev/tty', os.O_RDWR)

print('Press Return to continue...')
sys.stdin.readline()
print('Continuing')

# Disable the alarm
signal.setitimer(signal.ITIMER_REAL,0)
