import signal
# Test signal.setitimer. Other signal.set*timer functions are tested by
# test_signal.

def alarm_handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, alarm_handler)

interval = 1.0
signal.setitimer(signal.ITIMER_REAL, interval)
time.sleep(2.0)

interval = 0.5
signal.setitimer(signal.ITIMER_REAL, interval)
time.sleep(2.0)
signal.setitimer(signal.ITIMER_REAL, 0)

print("Done!")
