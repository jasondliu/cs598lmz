import signal
# Test signal.setitimer()


def handler(signum, frame):
    print("Got signal:", signum)
    raise OSError("got signal")


signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2)

for i in range(4):
    print("Sleeping", i)
    time.sleep(1)

print("Done")
