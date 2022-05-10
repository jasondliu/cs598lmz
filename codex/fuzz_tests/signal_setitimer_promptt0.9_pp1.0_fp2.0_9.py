import signal
# Test signal.setitimer
def handler(signum, frame):
    global handle_count
    handle_count += 1
    if handle_count > 2:
        print("handling too much, exit")
        sys.exit(0)

def test_signal():
    global handle_count
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 5, 0)

    time.sleep(30)

# Test signal.siginterrupt
def handler2(signum, frame):
    print("sigalrm handler")
    time.sleep(3)
    print("sigalrm handler done")

def test_siginterrupt():
    signal.signal(signal.SIGALRM, handler2)
    signal.siginterrupt(signal.SIGALRM, True)
    signal.setitimer(signal.ITIMER_REAL, 0.01, 0)
    while True:
        time.sleep(1)

if __name__ == "__main__":
