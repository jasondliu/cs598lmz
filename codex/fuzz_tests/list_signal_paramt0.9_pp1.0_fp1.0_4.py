import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        return
    signal.setitimer(signal.ITIMER_REAL, 0)
    print("{} real time expired itimers".format(N))


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    signals.setitimer(signal.ITIMER_REAL, delays.pop(0))
    print("started {} real time itimers of {}s total".format(N, sum(delays)))
    for i in range(N):
        pass
    print("done")
