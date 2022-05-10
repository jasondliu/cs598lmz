import signal
# Test signal.setitimer() and signal.getitimer()

def alarm_handler(signum, frame):
    print("Alarm triggered")

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Done")

signal.setitimer(signal.ITIMER_REAL, 0)
