import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print('\nDone')

def main():
    signal.signal(signal.SIGALRM, handler)
    handler()

if __name__ == '__main__':
    main()
