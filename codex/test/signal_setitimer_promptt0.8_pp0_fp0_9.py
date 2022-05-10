import signal
# Test signal.setitimer()


def handler(signum, frame):
    global count
    print("Hello World!", str(count))
    count += 1
    if count >= 10:
        signal.setitimer(signal.ITIMER_REAL, 0)  # disable ittimer


count = 0
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 1)  # realtime, first: 1, interval: 1

