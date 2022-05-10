import signal
# Test signal.setitimer() with SIGALRM
def setitimer_handler(signum, frame):
    print('SIGALRM')
    # Do not re-schedule alarm for now.

signal.signal(signal.SIGALRM, setitimer_handler)
val = signal.setitimer(signal.ITIMER_REAL, 0.5)
if val != (0, 0):
    raise SystemExit('SIGALRM not scheduled')
print('Sleeping for 3 seconds, expect 1 alarm')
time.sleep(3)
# Now schedule an alarm for 1 second.
signal.setitimer(signal.ITIMER_REAL, 1)
print('Sleeping for 3 seconds, expect 1 alarm')
time.sleep(3)
print('Done')
