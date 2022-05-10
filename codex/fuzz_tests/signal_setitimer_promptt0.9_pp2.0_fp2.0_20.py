import signal
# Test signal.setitimer to kill a thread.

def longtask():
    for i in range(10000000):
        pass

def handler(sig, frame):
    print('signal', sig)

def handler2(sig, frame):
    print('signal2', sig)
    raise RuntimeError("should exit with signal 2")

def thread1():
    print('started')
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.001, 0.001)
    try:
        longtask()
        print('should not get here')
    except KeyboardInterrupt:
        print('got KeyboardInterrupt')

def thread2():
    print('started')
    signal.signal(signal.SIGALRM, handler2)
    signal.setitimer(signal.ITIMER_REAL, 0.0001, 0.0001)
    longtask()
    print('should not get here')


# Create a thread that's going to receive SIGALRM
t = threading.Thread
