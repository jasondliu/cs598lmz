import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("Alarm raised")

def timer_handler(signum, frame):
    print("Timer expired")

signal.signal(signal.SIGALRM, alarm_handler)
signal.signal(signal.SIGVTALRM, timer_handler)

# Set an alarm to go off in 2 seconds
signal.setitimer(signal.ITIMER_REAL, 2)

# Set a 100 Hz timer going
signal.setitimer(signal.ITIMER_VIRTUAL, 1/100)

while True:
    pass
