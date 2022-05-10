import signal
# Test signal.setitimer

# Test that SIGALRM is delivered to the main thread even when the main
# thread is blocked in a system call.

# This test is Linux-specific.  It will hang on other platforms.

def handler(signum, frame):
    print('SIGALRM received')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# This will block until a SIGALRM is received.
os.read(0, 1)
