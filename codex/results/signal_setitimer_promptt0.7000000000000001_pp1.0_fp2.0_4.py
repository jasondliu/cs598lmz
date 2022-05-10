import signal
# Test signal.setitimer
def call_it(signum, frame):
    print(signum, frame)
signal.signal(signal.SIGALRM, call_it)
signal.setitimer(signal.ITIMER_REAL, 0.05, 0.01)

# Test signal.sigwaitinfo
signal.sigwaitinfo({signal.SIGTERM, signal.SIGINT})

# Test signal.getsignal
signal.getsignal(signal.SIGALRM)
