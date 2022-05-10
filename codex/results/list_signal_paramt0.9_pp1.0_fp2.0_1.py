import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        sys.exit()

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

    try:
        for i in range(N):
            enter = time.time()
            time.sleep(0)
            leave = time.time()
            print '%.9f' % (leave - enter)
        print
    except KeyboardInterrupt:
        pass

    handler()

if __name__ == '__main__':
    main()
