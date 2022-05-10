import signal
# Test signal.setitimer function
def handler(a, b):
    print("Got signal", a, b)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)
signal.setitimer(signal.ITIMER_REAL, 2)

# Test signals module
import signals
signals.on(signal.SIGALRM, handler)
signals.set_timer(signal.ITIMER_REAL, 2)
signals.set_timer(signal.ITIMER_REAL, 2)


# Test signal module API
def handler(a, b):
    print("Got signal", a, b)
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGALRM, signal.SIG_DFL)
signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.signal(signal.SIGALRM, signal.SIG_IGN)
