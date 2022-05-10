import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("Done.")
        sys.exit(0)

def main():
    # install alarm handler
    signal.signal(signal.SIGALRM, handler)
    # start 1st alarm
    handler()
    while delays:
        print("Do stuff.")
        time.sleep(0.01)

if __name__ == "__main__":
    main()
