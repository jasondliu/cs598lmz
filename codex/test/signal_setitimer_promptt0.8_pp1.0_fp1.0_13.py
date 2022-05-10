import signal
# Test signal.setitimer()
def t0():
    def g():
        print("g()")

    signal.setitimer(signal.ITIMER_REAL, 0.5)

    signal.signal(signal.SIGALRM, g)
    while 1:
        pass

# Test signal.alarm()
def t1():
    def g():
        print("g()")

    signal.signal(signal.SIGALRM, g)
    signal.alarm(1)
    while 1:
        pass

# Test signal.signal(SIGINT, SIG_IGN)
def t2():
    print("Test Ctrl-C only stop processes")
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    while True:
        pass

# Test signal.signal(SIGINT, SIG_IGN)
def t3():
    print("Test Ctrl-C only stop processes")

    def g(sig, frame):
        print("Ctrl-C is pressed")

