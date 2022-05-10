import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, howlong, 0)
# and signal.setitimer(signal.ITIMER_PROF, howlong, 0)
PROFFLAG = 1 << 16

def handler(signum, frame):
    now = time.time()
    print now - start, 'alarm'


if __name__ == '__main__':
    print 'Starting'
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)
    signal.setitimer(signal.ITIMER_PROF, 0.1, 0)
    start = time.time()
    for x in xrange(2):
        time.sleep(0.2)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0)
    signal.setitimer(signal.ITIMER_PROF, 0.1, 0)
    for x in xrange(2):
        time.sleep(0
