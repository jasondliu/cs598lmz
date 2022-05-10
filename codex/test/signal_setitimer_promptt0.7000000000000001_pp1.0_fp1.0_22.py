import signal
# Test signal.setitimer and signal.getitimer
#
# Note that signal.setitimer(signal.ITIMER_REAL, 0, 0) is a
# bit of an oddball test, since it's the only one that doesn't
# raise an exception when the interval is 0.

if not sys.platform.startswith(('freebsd', 'linux')):
    print('Unsupported platform %s' % sys.platform)
    sys.exit(0)

def alarm_handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 100, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 100)
signal.setitimer(signal.ITIMER_REAL, 0, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 1)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

