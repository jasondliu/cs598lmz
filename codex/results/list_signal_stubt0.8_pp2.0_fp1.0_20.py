import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print "finished"

def main():
    for delay in delays[:-1]:
        signal.setitimer(signal.ITIMER_REAL, delay)
        signal.pause()
    handler()

if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    main()
</code>

