import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("Timer is done.")

def main():
    handler()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
</code>
I really only need around 10-30Hz, but I'm afraid of consuming too much CPU and, more importantly, locking up my RaspPi.  How should I approach this?  Any help would be greatly appreciated.

