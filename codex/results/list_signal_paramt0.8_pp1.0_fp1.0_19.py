import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def main():
    # Sometimes my Mac shows the following error message:
    #
    #     Resource temporarily unavailable
    #
    # It seems I should ignore the error.
    signal.signal(signal.SIGALRM, handler)
    handler()
    while delays:
        pass

if __name__ == '__main__':
    main()
