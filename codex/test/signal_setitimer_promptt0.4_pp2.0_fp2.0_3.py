import signal
# Test signal.setitimer() with all values of the interval argument
# set to zero.  The signal should be delivered immediately.

def handler(signum, frame):
    print("handler")
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)

for i in range(5):
    print("setitimer", i)
    signal.setitimer(signal.ITIMER_REAL, 0)
    time.sleep(1)

print("OK")
