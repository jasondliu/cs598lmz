import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)
    else:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)
    while delays:
        # handle alarms
        signal.pause()

if __name__ == '__main__':
    import random
    import signal
    random.seed(1)
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    print "latency (ms):"
    main()
