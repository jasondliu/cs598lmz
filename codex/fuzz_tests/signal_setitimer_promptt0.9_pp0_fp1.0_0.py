import signal
# Test signal.setitimer()
CHILD = 2
INTERVAL = 0.1

def maybe_exit():
    if random.random() < INTERVAL:
        sys.exit(CHILD)

def handler(signum, frame):
    assert signum == signal.SIGALRM
    print('Signal handler called with signal', signum)
    maybe_exit()

for i in range(10):
    print('PARENT {}'.format(os.getpid()))
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, INTERVAL)
    maybe_exit()
    print('EXITING', os.getpid())
    exit(0)
