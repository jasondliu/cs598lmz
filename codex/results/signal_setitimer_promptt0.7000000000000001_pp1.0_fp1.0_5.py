import signal
# Test signal.setitimer
for sig in [signal.SIGALRM, signal.SIGPROF]:
    signal.signal(sig, lambda *args: None)
    signal.setitimer(sig, 1, 0)
    signal.setitimer(sig, 0, 0)


# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)
signal.set_wakeup_fd(-1)


# Test signal.getsignal
for s in [signal.SIGABRT, signal.SIGFPE, signal.SIGILL, signal.SIGINT,
          signal.SIGSEGV, signal.SIGTERM]:
    signal.getsignal(s)


# Test signal.pause
signal.pause()
