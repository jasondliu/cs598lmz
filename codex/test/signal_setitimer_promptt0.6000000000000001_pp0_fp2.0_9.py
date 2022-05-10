import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Alarm handler: ", signum, frame)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 1)

try:
    while True:
        print("Waiting for signal")
        signal.pause()
except KeyboardInterrupt:
    print("Caught keyboard interrupt")
