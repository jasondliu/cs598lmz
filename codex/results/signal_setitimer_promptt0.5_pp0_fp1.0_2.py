import signal
# Test signal.setitimer()
#
# The test is run as follows:
#
# - Install a handler for SIGALRM.
# - Set an alarm for 1 second, and note the time.
# - Wait for 5 seconds.
# - Check if the handler has been called, and if so, check the time.
#
# The expected result is that the handler is called exactly once, and that
# the time is approximately 1 second after the time noted above.
#
# The test is repeated with the ITIMER_VIRTUAL and ITIMER_PROF timers,
# and with the SA_RESTART flag.

def handler(signum, frame):
    global called, time_called
    called = True
    time_called = time.time()

def test(timer, flags):
    global called, time_called
    called = False
    time_called = 0
    signal.signal(signal.SIGALRM, handler)
    t0 = time.time()
    if flags:
        signal.siginterrupt(signal.SIGALRM, False)
    else:
        signal
