import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 10, 1) # ITIMER_REAL
signal.setitimer(signal.ITIMER_VIRTUAL, 10, 1) # ITIMER_VIRTUAL
signal.setitimer(signal.ITIMER_PROF, 10, 1) # ITIMER_PROF

def handler(signum, frame):
    print("Signal handler called with signal", signum)

signal.signal(signal.SIGALRM, handler)

while True:
    signal.pause()
# Test signal.getsignal()
print("SIGINT handler:", signal.getsignal(signal.SIGINT))
print("SIGUSR1 handler:", signal.getsignal(signal.SIGUSR1))
# Test signal.getsignal()
signal.getsignal(signal.SIGINT)
# Test signal.getsignal()
def handler(signum, frame):
    print("SIGUSR1 handler called with frame:
