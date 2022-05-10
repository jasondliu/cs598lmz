import signal
# Test signal.setitimer
def handler(signum, frame):
    print signum
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 1)
time.sleep(5)
# Test signal.siginterrupt
signal.siginterrupt(signal.SIGINT, False)
signal.siginterrupt(signal.SIGINT, True)
# Test signal.sigpending
signal.sigpending()
# Test signal.sigwait
signal.sigwait([signal.SIGINT])
# Test signal.sigwaitinfo
signal.sigwaitinfo([signal.SIGINT])
# Test signal.strsignal
signal.strsignal(signal.SIGINT)
# Test signal.getsignal
signal.getsignal(signal.SIGINT)
# Test signal.set_wakeup_fd
signal.set_wakeup_fd(0)
# Test signal.pause
signal.pause()
# Test
