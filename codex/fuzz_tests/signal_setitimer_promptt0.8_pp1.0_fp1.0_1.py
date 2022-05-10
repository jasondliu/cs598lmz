import signal
# Test signal.setitimer
def test_setitimer_basic():
    tmp = signal.setitimer(signal.ITIMER_REAL, 1, 2)
    assert tmp[0] == 0.0, repr(tmp[0])
    assert tmp[1] == 0.0, repr(tmp[1])
    signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Skip very slow tests if signal.setitimer is not available
if hasattr(signal, 'setitimer'):
    def timer_handler(signum, frame):
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
        raise KeyboardInterrupt

    prev_handler = signal.signal(signal.SIGALRM, timer_handler)

    def test_setitimer_real():
        signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
        # this should return immediately and then raise
        # KeyboardInterrupt after half a second
        time.sleep(1)
        signal.setitimer(
