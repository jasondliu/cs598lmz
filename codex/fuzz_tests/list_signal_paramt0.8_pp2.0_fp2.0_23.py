import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print "Catch signal %d" % signum

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 1e-6)

    for i in range(N):
        try:
            time.sleep(0.01)
        except:
            pass

if __name__ == '__main__':
    main()
