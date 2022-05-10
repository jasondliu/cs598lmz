import signal
# Test signal.setitimer() with ITIMER_VIRTUAL

def handler(signum, frame):
    global hits
    hits += 1

signal.signal(signal.SIGVTALRM, handler)
hits = 0
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)

t0 = time.time()
while time.time() - t0 < 3:
    pass

signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)

if hits < 2:
    print("FAIL: setitimer(ITIMER_VIRTUAL)")
else:
    print("PASS")
