import signal
# Test signal.setitimer/signal.getitimer, as well as siginterrupt.
# Use a timeout.  This can take a while to run.
import time
int_count = 0
def alarm_handler(signum, frame):
    global int_count
    int_count += 1
    print(int_count, 'CLOCK', time.clock())
    time.sleep(0.1)
    if int_count == 3:
        raise SystemExit
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 2.0, 2.1)
print(time.clock())
time.sleep(10)
# Hm, the 2.0 ITIMER_REAL case sometimes gets sigint, sometimes not.
# Followup tests show that:
#  - siginterrupt is mostly effective (except for 1 or 2 cases) if called
#    before setitimer.
#  - 1.0 ITIMER_REAL also gets it right most of the time.
#  - Both 1.0 and 2.0
