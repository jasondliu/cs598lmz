import signal
# Test signal.setitimer(), signal.getitimer() and signal.alarm()

# This is a test for issue #14073

def handler(signum, frame):
    print('handler')

signal.signal(signal.SIGALRM, handler)

# setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.2)
signal.setitimer(signal.ITIMER_PROF, 0.3)

# getitimer()
print(signal.getitimer(signal.ITIMER_REAL))
print(signal.getitimer(signal.ITIMER_VIRTUAL))
print(signal.getitimer(signal.ITIMER_PROF))

# alarm()
signal.alarm(1)

# Block the alarm signal
signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGALRM})

# alarm
