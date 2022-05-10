import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def main():
    signal.signal(signal.SIGALRM, handler)

    # Prime the pump.
    signal.setitimer(signal.ITIMER_REAL, delays.pop())

    for i in range(N):
        print i

    print 'Done'

if __name__ == '__main__':
    main()
