import signal
# Test signal.setitimer() for a different period of time
def alarm_handler(signum, frame):
    "handler"
