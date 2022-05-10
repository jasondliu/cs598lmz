import signal
# Test signal.setitimer() and signal.getitimer().
import errno

def handler1(signum, frame):
    print("handler1 called")

def handler2(signum, frame):
    print("handler2 called")

def handler3(signum, frame):
    raise KeyboardInterrupt

def test_main():
    signal.signal(signal.SIGALRM, handler1)
    signal.signal(signal.SIGALRM, handler2)
    signal.alarm(2)
    signal.setitimer(signal.ITIMER_REAL, 1, 1)
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    try:
        signal.pause()
    except KeyboardInterrupt:
        pass
    signal.signal(signal.SIGALRM, handler3)
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
    signal.alarm(2)
    try:
        signal.pause()
    except KeyboardInterrupt:
        pass
    try
