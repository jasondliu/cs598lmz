import signal
# Test signal.setitimer() and signal.getitimer()
def handler(signum, frame):
    print("got signal", signum)
    print("frame", frame)
    print("time", time.asctime())
    signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
print("setting timer")
signal.setitimer(signal.ITIMER_REAL, 1, 1)
print("time", time.asctime())
print("sleeping")
time.sleep(10)
print("done sleeping")

print("getitimer", signal.getitimer(signal.ITIMER_REAL))

# Test signal.setitimer() and signal.getitimer()
def handler(signum, frame):
    print("got signal", signum)
    print("frame", frame)
    print("time", time.asctime())
    signal.setitimer(signal.ITIMER_VIRTUAL, 0)

