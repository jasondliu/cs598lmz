import signal
# Test signal.setitimer() with the ITIMER_REAL timer.
def handler(*args):
    print 'handler', args
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
print 'start'
time.sleep(0.5)
print 'stop'

# Test signal.setitimer() with the ITIMER_VIRTUAL timer.
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.2)
print 'start'
time.sleep(0.5)
print 'stop'

# Test signal.setitimer() with the ITIMER_PROF timer.
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.2)
print 'start'
time.sleep(0.5)
print 'stop'

# Test signal.setitimer() with a negative first argument.
try:
    signal.setitimer(signal.ITIMER_REAL, -
