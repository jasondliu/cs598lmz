import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 1)
signal.setitimer(signal.ITIMER_PROF, 0.5, 1)

def handler(signum, frame):
    print 'signum:', signum, '\nframe:', frame

signal.signal(signal.SIGALRM, handler)

# test signal.signal()
#signal.signal(signal.SIGALRM, handler)

# test signal.alarm()
#signal.alarm(1)

# test signal.pause()
#signal.pause()

# test signal.setitimer()
#signal.setitimer(signal.ITIMER_REAL, 0.5, 1)
#signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 1)
#signal.setitimer(signal.ITIM
