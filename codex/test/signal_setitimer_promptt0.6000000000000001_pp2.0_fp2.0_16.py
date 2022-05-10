import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
#
# Expected behavior:
# - timer is set to 1 second
# - itimer fires after 1 second
# - program exits

def handler(signum, frame):
    raise SystemExit

signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)

