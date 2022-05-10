import signal
# Test signal.setitimer() and signal.getitimer().

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise SystemExit

signal.signal(signal.SIGALRM, handler)

# Set an alarm.
signal.setitimer(signal.ITIMER_REAL, 0.2)

print('About to sleep')
time.sleep(1)
print('Done')
