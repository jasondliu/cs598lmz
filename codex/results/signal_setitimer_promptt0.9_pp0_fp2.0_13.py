import signal
# Test signal.setitimer() using SIGALRM with itimer_value != 0.0
def handle_alarm(signum, frame):
    print("Got signal %d" % signum)

signal.signal(signal.SIGALRM, handle_alarm)
alarmtime = 5.0
signal.setitimer(signal.ITIMER_REAL, alarmtime, 0.0)
time.sleep(10.0)
