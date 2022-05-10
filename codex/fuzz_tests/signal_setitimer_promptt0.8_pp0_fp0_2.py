import signal
# Test signal.setitimer() and signal.alarm() (which are different).

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

signal.signal(signal.SIGALRM, alarm_handler)

print "testing signal module"

# First make sure SIGALRM doesn't get delivered prematurely
signal.alarm(2)
time.sleep(1)
signal.alarm(2)

# Now check if SIGALRM gets delivered approximately on time
signal.signal(signal.SIGALRM, alarm_handler)
for i in range(1, 10):
    delay = 0.1 ** i
    signal.alarm(int(delay))
    try:
        time.sleep(delay + 0.1)
    except Alarm:
        print "alarm", delay
        continue
    else:
        print "no alarm (%.1f sec)" % delay
        break
    finally:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

# Now check if
