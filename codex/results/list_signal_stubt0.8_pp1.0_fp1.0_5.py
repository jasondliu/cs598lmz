import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def main():
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    signal.signal(signal.SIGALRM, handler)
    while delays:
        pass

if __name__ == '__main__':
    main()
</code>
on my computer this takes about 0.43s.
instead, if I remove the while delays: pass loop and just let the program finish, it takes 1.41s.
If I change the signal handler to set the timeout to a fixed value (say 0.1ms), then run the program and measure the time it takes, it takes about 0.8s.
It seems that a lot of the time is being wasted on setting the interrupt timer. 
Is there anything I can do about this? like batching the calls to signal.setitimer, or using a different signal (even if it means I have to use threads)
EDIT:
Answering the questions from the comments
<code>import signal
import timeit

def handler(num, frame):
    pass

def main():
    signal.setitimer(
