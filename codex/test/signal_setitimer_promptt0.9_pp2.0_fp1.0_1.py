import signal
# Test signal.setitimer
numer_of_halt = 0


def handle_timeout(signum, frame):
    global numer_of_halt
    numer_of_halt += 1
