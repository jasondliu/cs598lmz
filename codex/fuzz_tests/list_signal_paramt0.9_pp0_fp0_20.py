import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
    else:
        print("no more to run")

def delaying():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)

def f():
    print("uuh!")

def g():
    print("ugh...")

def h(num=None, frame=None):
    print("got signal {}".format(num))

def j():
    print("hi")

def main():
    passing(delaying(), f, g)
    passing(delaying(), h, passing, signal.SIGALRM, j)

if __name__ == "__main__":
    main()
