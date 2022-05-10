import signal
# Test signal.setitimer() and signal.getitimer()
#
# This test is a little different from the others, because it
# doesn't just check that an API call works, but that it works
# correctly.  So we have to do a little more work.

# This function is called when the alarm goes off.  It just sets a flag
# to tell the main program that the alarm went off.
alarm_flag = False
def alarm_handler(signum, frame):
    global alarm_flag
    alarm_flag = True

# Call signal.setitimer() and signal.getitimer() with various arguments.
# For each call, check that the timer was set correctly, and that the
# signal handler was called at the right time.
def test_setitimer():
    global alarm_flag
    for interval in [0.1, 0.2, 0.5, 1.0]:
        for value in [0.1, 0.2, 0.5, 1.0]:
            signal.signal(signal.SIGALRM, alarm_handler)
            alarm_flag = False
            signal.set
