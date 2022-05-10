import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        print("signum = %s, frame = %s" %(signum, frame))

def main():
    print(signal.getitimer(signal.ITIMER_REAL))
    signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    signal.signal(signal.SIGALRM, handler)
    print(signal.getitimer(signal.ITIMER_REAL))
    try:
        while True:
            time.sleep(1)
    except:
        pass

if __name__ == "__main__":
    main()
