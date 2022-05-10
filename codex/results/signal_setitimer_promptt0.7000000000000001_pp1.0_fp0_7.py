import signal
# Test signal.setitimer for SIGPROF

signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

def handler(signum, frame):
    if signum == signal.SIGALRM:
        print("got SIGALRM")
    elif signum == signal.SIGPROF:
        print("got SIGPROF")
    else:
        assert False

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGPROF, handler)
# catch SIGALRM with SIG_IGN: no handler executed
signal.signal(signal.SIGALRM, signal.SIG_IGN)
# check that SIGPROF handler is executed
# (as SIGALRM is ignored, the SIGPROF handler will run)
signal.alarm(1)

# wait for signals
try:
    for i in range(3):
        time.sleep(1)
except KeyboardInterrupt:
    pass
