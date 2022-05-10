import signal
# Test signal.setitimer()
def setitimer():
    def handler(signum, frame):
        print('signum =', signum)
        print(time.time())

    signal.signal(signal.SIGALRM, handler)

    signal.setitimer(signal.ITIMER_REAL, 3)
    time.sleep(5)

# Test signal.setitimer()
def setitimer_2():
    def handler(signum, frame):
        print('signum =', signum)
        print(time.time())

    signal.signal(signal.SIGALRM, handler)

    signal.setitimer(signal.ITIMER_REAL, 3, 1)
    time.sleep(5)

# Test signal.setitimer()
def setitimer_3():
    def handler(signum, frame):
        print('signum =', signum)
        print(time.time())

    signal.signal(signal.SIGALRM, handler)

