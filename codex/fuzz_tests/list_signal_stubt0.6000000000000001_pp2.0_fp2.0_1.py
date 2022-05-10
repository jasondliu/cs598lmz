import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def set_timer():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())

def main():
    set_timer()
    for i in range(N):
        print('.', end='', flush=True)
    print()

if __name__ == '__main__':
    main()
