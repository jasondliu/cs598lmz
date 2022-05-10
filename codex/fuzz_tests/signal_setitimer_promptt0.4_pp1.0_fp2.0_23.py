import signal
# Test signal.setitimer()
#
# This tests that the signal module can be used to set a timer
# that will interrupt the Python interpreter.  It also tests
# that the timer can be cancelled.

def alarm_handler(signum, frame):
    print("alarm_handler")
    raise SystemExit

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)

print("Sleeping for 1 second")
time.sleep(1)

print("Setting the timer to 0.1 seconds")
signal.setitimer(signal.ITIMER_REAL, 0.1)

print("Sleeping for 1 second")
time.sleep(1)

print("Cancelling the timer")
signal.setitimer(signal.ITIMER_REAL, 0)

print("Sleeping for 1 second")
time.sleep(1)

print("Done")
