import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def timeout(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("timed out!")

def main():
    print 'starting:', time.time()
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        signal.pause()
    signal.setitimer(signal.ITIMER_REAL, 0)

main()
