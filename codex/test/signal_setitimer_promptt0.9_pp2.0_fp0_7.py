import signal
# Test signal.setitimer() with SIGVTALRM.
def handler(signum, frame):
    print('Call handler()')
# call handler 1 seconds later
signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
time.sleep(10)  # after 10 seconds, handler should be called once.
