import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, min(delays))
        delays.pop(0)

def run(func):
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, min(delays))

    try:
        func()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)

def main():
    run(lambda: [i*2 for i in range(N)])

main()
