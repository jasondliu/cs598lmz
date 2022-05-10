import signal
# Test signal.setitimer with all possible values for the interval

def handler(signum, frame):
    print("signal", signum)
    if signum == signal.SIGALRM:
        print("SIGALRM")
    elif signum == signal.SIGPROF:
        print("SIGPROF")
    else:
        print("unknown")
    print("frame", frame)

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGPROF, handler)

for i in (-1, 0, 1e-6, 1, 10, 100, 1000, 10000, 100000):
    print("interval: %g" % i)
    signal.setitimer(signal.ITIMER_REAL, i, 0)
    sleep(0.1)

print("done")
