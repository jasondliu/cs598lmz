import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)

# Test signal.setitimer with a list of signals.
signal.setitimer([signal.ITIMER_VIRTUAL, signal.ITIMER_PROF], 0.1)

# Test signal.setitimer with a dict of signals.
signal.setitimer({signal.ITIMER_VIRTUAL: 0.1, signal.ITIMER_PROF: 0.2})

# Test signal.setitimer with an iterable of signals.
signal.setitimer(iter([signal.ITIMER_VIRTUAL, signal.ITIMER_PROF]), 0.1)
