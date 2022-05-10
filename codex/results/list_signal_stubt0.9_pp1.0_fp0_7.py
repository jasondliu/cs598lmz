import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("DONE!")
        raise SystemExit()

def main():
    print("START!")
    signal.signal(signal.ITIMER_REAL, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        pass

if __name__ == '__main__':
    main()
