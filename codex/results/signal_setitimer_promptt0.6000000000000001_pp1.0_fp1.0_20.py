import signal
# Test signal.setitimer
#
# To test this module, run it under the control of a debugger
# which can stop on a breakpoint.
#
# The test will run to completion.

def alarm_handler(signum, frame):
    raise ValueError("Signal handler called")

if __name__ == "__main__":
    # Set up a signal handler
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
    # Now run to completion.
