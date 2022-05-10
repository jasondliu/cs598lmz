import signal
# Test signal.setitimer()
def signalcatcher(sig, stack):
    print("Caught signal", sig)
    print("Scheduler delay", itimer.delay)
    assert sig == signal.SIGALRM
    assert itimer.delay == 0.25
    assert itimer.value == 0.5
    itimer.delay = 0.5
    itimer.value = 1

signal.signal(signal.SIGALRM, signalcatcher)
itimer = signal.setitimer(signal.ITIMER_REAL, 0.5, 0.25)
print("Initial scheduler delay", itimer.delay)
assert itimer.delay == 0
assert itimer.value == 0.5
time.sleep(1.5)
print("Final scheduler delay", itimer.delay)
assert itimer.delay == 0.5
assert itimer.value == 1
