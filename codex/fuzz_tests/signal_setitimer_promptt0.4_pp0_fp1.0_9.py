import signal
# Test signal.setitimer()

def handle_alarm(signum, frame):
    print("Got SIGALRM")

signal.signal(signal.SIGALRM, handle_alarm)

signal.setitimer(signal.ITIMER_REAL, 0.1)

signal.pause()
