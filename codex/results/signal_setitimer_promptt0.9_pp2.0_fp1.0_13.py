import signal
# Test signal.setitimer, allowing to send itimeouts to a python process
def handler(signum, frame):
    print "test frame =", frame
    raise Exception("test")

signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)

while True:
    time.sleep(1)
    print "tick"
