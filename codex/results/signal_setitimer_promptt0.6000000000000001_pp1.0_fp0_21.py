import signal
# Test signal.setitimer(signal.ITIMER_REAL, 1, 0)

def handler(signum, frame):
    print("Alarm handler called")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1, 0)

print("Sleeping for 2 seconds")
signal.pause()
print("Done sleeping")

print("Sleeping for 2 seconds")
time.sleep(2)
print("Done sleeping")
