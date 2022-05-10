import signal
# Test signal.setitimer
def handler(signum, frame):
    print("Alarm")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 2)

# Test signal.setitimer
# def handler(signum, frame):
#     print("Alarm")

# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_REAL, 1)

# Test signal.setitimer
# def handler(signum, frame):
#     print("Alarm")

# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_VIRTUAL, 1)

# Test signal.setitimer
# def handler(signum, frame):
#     print("Alarm")

# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_PROF, 1)

# Test signal.
