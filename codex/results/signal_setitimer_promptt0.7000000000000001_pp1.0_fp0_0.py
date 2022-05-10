import signal
# Test signal.setitimer

# This test attempts to do something similar to the test in
# Lib/test/test_signal.py.

def alarm_handler(signum, frame):
    global alarm_fired
    alarm_fired = True

def setitimer_handler(signum, frame):
    global setitimer_fired
    setitimer_fired = True

def test_setitimer():
    global alarm_fired, setitimer_fired
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.signal(signal.SIGVTALRM, setitimer_handler)

    alarm_fired = False
    signal.alarm(1)
    time.sleep(2)
    if not alarm_fired:
        print("FAILURE: alarm was not raised")
        return False

    setitimer_fired = False
    signal.setitimer(signal.ITIMER_VIRTUAL, 1)
    time.sleep(2)
    if not setitimer_fired:
        print("FAILURE: setitimer was not raised
