import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 1, .1)

def signal_handler(signum, frame):
    print "signal_handler:", signum, frame
    return

signal.signal(signal.SIGVTALRM, signal_handler)

# signal.alarm(0)  # disable
# signal.alarm(2)  # enable
signal.setitimer(signal.ITIMER_VIRTUAL, 1, .1)
# signal.setitimer(signal.ITIMER_REAL, 1, .1)

for i in range(100):
    print ".",
    time.sleep(.2)
