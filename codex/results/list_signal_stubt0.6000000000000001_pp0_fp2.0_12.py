import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

def main():
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        i = 0
        while i < N:
            i += 1
    print "Done!"

main()

# vim: et sw=4 sts=4
