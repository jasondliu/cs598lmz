import signal
# Test signal.setitimer
for timer in (signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF):
    # on windows, only ITIMER_REAL works
    if timer == signal.ITIMER_VIRTUAL and sys.platform == "win32":
        continue
    if timer == signal.ITIMER_PROF and sys.platform == "win32":
        continue
    def handler(signum, frame):
        assert signum in (signal.SIGALRM, signal.SIGVTALRM, signal.SIGPROF)

    signal.signal(signal.SIGALRM, handler)
    signal.signal(signal.SIGVTALRM, handler)
    signal.signal(signal.SIGPROF, handler)
    signal.setitimer(timer, interval=0.03, value=0)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(-1)
signal.set_wakeup_fd(-2)

try:
    os
