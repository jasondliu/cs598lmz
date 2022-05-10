import signal
# Test signal.setitimer()
def handler(n, frame):
        print('timer expired')
        # see man setitimer(2)
        signal.setitimer(signal.ITIMER_REAL, 0)

###signal.setitimer(signal.ITIMER_REAL, 1)
###signal.signal(signal.SIGALRM, handler)

# Test signal.sigpending()
def handler2(n, frame):
        print('sigpending test:', signal.sigpending())
        # only raises SIGINT once
        signal.signal(signal.SIGINT, handler2)

###signal.signal(signal.SIGINT, handler2)
