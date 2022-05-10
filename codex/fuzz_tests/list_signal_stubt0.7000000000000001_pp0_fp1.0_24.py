import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print 'tick', len(delays)


def main():
    # Install the signal handler and set the signal timer
    for sig in [signal.SIGALRM, signal.SIGVTALRM, signal.SIGPROF]:
        signal.signal(sig, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
    while delays:
        time.sleep(1)


if __name__ == '__main__':
    main()
