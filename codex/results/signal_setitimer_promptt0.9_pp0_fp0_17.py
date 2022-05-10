import signal
# Test signal.setitimer

signal.setitimer.restype = None

result = signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
if result == NotImplementedError:
    raise SkipTest("setitimer is not implemented")

def on_timer(*args):
    pass

signal.signal(signal.ITIMER_VIRTUAL, on_timer)
