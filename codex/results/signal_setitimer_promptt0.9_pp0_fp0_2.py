import signal
# Test signal.setitimer()
# Argument time is time interval in seconds for which real time must have elapsed without being interrupted.
# Argument interval is time interval in seconds after which the handler is called again.

def signal_handler(num, frame):
# It will get called each second
    print("Signal: ", num)

signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
    signal.pause()
