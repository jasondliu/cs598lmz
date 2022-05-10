import signal
# Test signal.setitimer
# See http://bugs.python.org/issue13918
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.set_wakeup_fd
# See http://bugs.python.org/issue13919
signal.set_wakeup_fd(12345)
