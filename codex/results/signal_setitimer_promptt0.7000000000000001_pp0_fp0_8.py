import signal
# Test signal.setitimer and signal.getitimer

def alarm_handler(signum, frame):
    print("alarm_handler: called at", time.ctime())
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 5, 0)

# Wait for the first alarm to go off.
print("Sleeping at", time.ctime())
time.sleep(1)
print("Sleeping some more at", time.ctime())
time.sleep(1)
print("Done sleeping")
