import signal
# Test signal.setitimer time format.

def handle(a,b):
    print('In signal handler')
    raise RuntimeError('ooh')

def wait(total):
    x = 0
    for i in range(100000):
        x += i*i
    time.sleep(total)

signal.signal(signal.SIGALRM, handle)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1)

signal.setitimer(signal.ITIMER_REAL, 0.0, 0.1)
wait(0.05)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
wait(0.05)
signal.setitimer(signal.ITIMER_REAL, 0.0, 0)
time.sleep(0.1)

signal.setitimer(signal.ITIMER_REAL, 10000.0)

