import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)
# It works with ITIMER_VIRTUAL, ITIMER_VIRTUAL, and ITIMER_REAL
# But it only works with 0.1, not 0.01, 0.001, or 0.0001
# It works with 0.1, and 0.5, but not 1.0, or 2.0
# Something is not quite right here.
# Try it with a different timer.
# Nope, 0.001 works.
# Try increasing the number of iterations on the infinite loop
# Nope, it works with 1,000,000,000, but not 1,000,000,000,000

# Try it with a different machine.
# Nope, it works on kirby, but not on kirby2.

# Try it with a different version of python.
# Nope, it works with python2.7.6 but not python2.7.3

# There's an infinite loop
def handler(signum, frame):
    print('sighandler invoked')

# Register handler
signal
