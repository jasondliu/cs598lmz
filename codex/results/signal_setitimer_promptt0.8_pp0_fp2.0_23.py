import signal
# Test signal.setitimer where this should be handled as a special
# case (if HP-UX)
if (signal.setitimer(signal.ITIMER_REAL, .1)):
    print("setitimer successful");
else:
    print("setitimer not successful");
