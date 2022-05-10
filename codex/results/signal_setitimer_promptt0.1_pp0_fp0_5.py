import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Signal handler called with signal", signum)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5)

# This open() may hang indefinitely
fd = os.open('/dev/ttyS0', os.O_RDWR)

# Press Ctrl+C to deliver a SIGINT
# Press Ctrl+\ to deliver a SIGQUIT
# Press Ctrl+Z to deliver a SIGTSTP

# After 5 seconds, a SIGALRM signal is sent
# and the handler is called.
# The alarm is not reset by the handler,
# and another SIGALRM is sent 5 seconds later.
# A further 5 seconds later, the handler is called again.
# This repeats until the program ends.

# The open() call, meanwhile, is unaffected by the signals.
# It does not return until the serial device is ready.
# This is because the signals are delivered to the main thread,
#
