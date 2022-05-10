import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 0.5)
signal.setitimer(signal.ITIMER_PROF, 0.5, 0.5)

# Test signal.set_wakeup_fd()
if sys.platform.startswith('linux'):
    # Not supported on all platforms
    fd = os.open(test.support.TESTFN, os.O_WRONLY | os.O_CREAT)
    signal.set_wakeup_fd(fd)
    signal.set_wakeup_fd(-1)
    os.close(fd)

# Test alarm()
signal.alarm(1)
signal.alarm(0)

# Test getsignal()
signal.getsignal(signal.SIGALRM)
signal.getsignal(signal.SIGUSR1)
try:
    signal.getsignal(-1
