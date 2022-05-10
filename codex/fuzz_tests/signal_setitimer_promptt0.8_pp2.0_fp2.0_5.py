import signal
# Test signal.setitimer
# Requires setting the alarm signal to execute a function
signal.signal(signal.SIGALRM, lambda signum, frame: None)

# Test signal.siginterrupt
try:
    signal.signal(signal.SIGINT, lambda signum, frame: None)
except ValueError:
    print("SKIP")
    raise SystemExit

# Test signal.set_wakeup_fd
# The function does nothing on CPython if the fd can't be set
signal.set_wakeup_fd(sys.stdout.fileno())
