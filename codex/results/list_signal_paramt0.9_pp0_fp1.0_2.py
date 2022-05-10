import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop())

def main():
    signal.signal(signal.SIGVTALRM, handler)
    signal.setitimer(signal.ITIMER_PROF, 1e-6)
    signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop())

    while delays:
        signal.pause()

    signal.setitimer(signal.ITIMER_VIRTUAL, 0)
    signal.setitimer(signal.ITIMER_PROF, 0)
    print("\nDone.")

if __name__ == "__main__":
    main()
