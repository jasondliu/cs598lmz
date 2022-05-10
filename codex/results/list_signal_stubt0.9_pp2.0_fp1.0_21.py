import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("done.")
        sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    i = 0
    print(datetime.datetime.now())
    while delays or i < N*:
        i += 1
        if delays:
            signal.setitimer(signal.ITIMER_REAL, delays.pop())
