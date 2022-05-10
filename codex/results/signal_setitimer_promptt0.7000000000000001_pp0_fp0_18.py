import signal
# Test signal.setitimer()

def alarm_handler(signum, frame):
    print("alarm")

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
signal.signal(signal.SIGALRM, alarm_handler)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0.4, 0.4)
signal.signal(signal.SIGVTALRM, alarm_handler)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 0.6, 0.6)
signal.signal(signal.SIGPROF, alarm_handler)

while True:
    time.sleep(1)
