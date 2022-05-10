import signal
# Test signal.setitimer.

def test_setitimer():
    prev = signal.signal(signal.SIGALRM, lambda signum, frame: 1/0)
    try:
        # Issue #13202: ValueError raised as RuntimeError on MacOSX Snow
        # Leopard
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
        prev = signal.setitimer(signal.ITIMER_REAL, 1e-6, 0)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)
    finally:
        signal.signal(signal.SIGALRM, prev)

def test_main():
    test_setitimer()

if __name__ == '__main__':
    test_main()
