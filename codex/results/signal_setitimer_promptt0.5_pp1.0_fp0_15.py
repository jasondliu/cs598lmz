import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Got alarm")

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)

print("Sleeping")
time.sleep(5)
print("Done sleeping")
