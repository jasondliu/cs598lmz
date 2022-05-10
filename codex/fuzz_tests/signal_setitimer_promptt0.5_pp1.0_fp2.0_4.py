import signal
# Test signal.setitimer()

def handler(signum, frame):
    print 'Alarm!'
    raise OSError

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2)

try:
    for i in range(5):
        print 'Loop %d' % i
        time.sleep(1)
except OSError:
    pass

signal.setitimer(signal.ITIMER_REAL, 0)

# Test signal.signal()

def handler(signum, frame):
    print 'Signal handler called with signal', signum

for sig in [signal.SIGABRT, signal.SIGFPE, signal.SIGILL, signal.SIGINT,
            signal.SIGSEGV, signal.SIGTERM]:
    signal.signal(sig, handler)

# Test signal.getsignal()

if signal.getsignal(signal.SIGINT) != handler:
    print 'getsignal
