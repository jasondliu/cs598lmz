import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        sys.stdout.write("\n")
        sys.stdout.flush()
        sys.exit(0)

def main():
    handler()
    signal.signal(signal.SIGALRM, handler)
    while True:
        pass

if __name__ == "__main__":
    main()
