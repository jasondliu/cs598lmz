import signal
# Test signal.setitimer()
signal.signal(signal.SIGALRM, lambda signum, frame: None)

if hasattr(signal, "setitimer"):
    # doesn't exist on Windows, but that's OK
    signal.setitimer(signal.ITIMER_PROF, 0.01, 0)
    time.sleep(0.1)

# Test signal.siginterrupt()
signal.siginterrupt(signal.SIGALRM, True)
signal.siginterrupt(signal.SIGALRM, False)

# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(-1)
if os.name == "nt":
    signal.set_wakeup_fd(-2)
signal.set_wakeup_fd(1)
if os.name == "nt":
    signal.set_wakeup_fd(2)
