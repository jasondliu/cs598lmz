import signal
# Test signal.setitimer()
def alarm_handler(signum, frame):
    print("handling alarm")
    sys.exit(0)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass


# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(sys.stdout.fileno())
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    pass
