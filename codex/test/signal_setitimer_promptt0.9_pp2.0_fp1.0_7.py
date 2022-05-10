import signal
# Test signal.setitimer on platforms that have it
from signal import setitimer, ITIMER_REAL
if hasattr(signal, "setitimer"):
    # Ensure that the signal is delivered in 2.2
    def handler(signum, frame):
        n.append(1)
    n = []
    setitimer(ITIMER_REAL, 0.1, 0.1) # Minimum unit on this platform: 1e-05
    signal.signal(signal.SIGALRM, handler)
    old = signal.signal(signal.SIGALRM, handler)
    # This loop gives the alarm a chance to be delivered, as it
    # depends on the vagaries of the OS thread scheduler.  If the
    # test fails, it almost always fails in the first iteration
    for i in range(100):
        if n:
            break
        time.sleep(0.01)
    else:
        raise RuntimeError("setitimer not functional")
    setitimer(ITIMER_REAL, 0, 0)
    # We need to deliver events that have been
