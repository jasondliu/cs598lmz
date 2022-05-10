import signal
# Test signal.setitimer()
# Verify the signal is received and handled properly
subsecs = 0.01
for delta in [0.01, 0.1, 1.0]:
    intval = int(delta)
    millisecs = int(delta*1000 - intval * 1000)
    signum = signal.SIGALRM
    if hasattr(signal, "SIGUSR1"):
        signum = signal.SIGUSR1
    timeout = 0.0

    def handler(signum, frame):
        global timeout
        timeout = time.time()

    signal.signal(signum, handler)

    # Repeat a few times to test accuracy
    start = time.time()
    signal.setitimer(signum, delta, 0.0)
    while timeout == 0.0:
        pass
    end = time.time()

    timed = end - start
    diff = timed - delta
