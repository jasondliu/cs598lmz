import signal
# Test signal.setitimer

def handler(signum, frame):
    print("handler:", signum)
    signal.setitimer(signal.ITIMER_REAL, 1.0, 0)

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 1.0, 0)

    while True:
        pass

main()
