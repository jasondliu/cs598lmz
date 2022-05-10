import signal
# Test signal.setitimer
def handler(a, b):
    pass
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, handler)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(-1)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(sys.stdout.fileno())
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(sys.stdout)
