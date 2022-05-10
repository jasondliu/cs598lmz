import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Alarm handler")

signal.signal(signal.SIGALRM, alarm_handler)

# signal.setitimer(signal.ITIMER_REAL, interval, interval)
# signal.setitimer(signal.ITIMER_VIRTUAL, interval, interval)
# signal.setitimer(signal.ITIMER_PROF, interval, interval)
signal.setitimer(signal.ITIMER_REAL, 5, 0)

while True:
    time.sleep(1)
    print(".", end="")
    sys.stdout.flush()
