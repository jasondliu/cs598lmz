import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Got signal %s at %s" % (signum, frame))
    raise SystemExit

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)

while True:
    print("Tick")
    time.sleep(1)
