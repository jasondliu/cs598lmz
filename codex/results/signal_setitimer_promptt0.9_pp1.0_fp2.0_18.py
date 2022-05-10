import signal
# Test signal.setitimer().

def handler(signal, frame, itimer):
    print(signal, frame, itimer.getvalue())
    assert itimer.getvalue()[0] == 0
    assert itimer.getvalue()[1] == 1e-6

signal.signal(signal.SIGPROF, handler)
itimer = signal.itimer(signal.ITIMER_PROF, 0, 1e-6)
time.sleep(2)
