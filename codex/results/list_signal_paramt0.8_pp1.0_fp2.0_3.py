import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    while delays:
        time.sleep(1)

if __name__ == '__main__':
    main()
</code>
Is it possible to improve performance of the code? I'm using Python 2.6.5.


A:

No, it is not possible to improve the performance of this code. It is doing work in the handler for each alarm.
Another problem with the code is that there is little time guarantee that a given alarm will be serviced at the time it should have been, because it requires the <code>time.sleep()</code> to complete. With a short sleep (1 second), you probably aren't going to run into problems with this.

