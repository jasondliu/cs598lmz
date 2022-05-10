import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        pass

if __name__ == '__main__':
    main()
</code>
The code above schedules the timers using <code>setitimer()</code>, which is signal-based, so it should have slightly less overhead.
If you're not constrained to Python, you can use Linux's <code>timerfd</code> feature, which allows you to create a file descriptor that can be used to wait for expiration of a timer.  Describing the interface is beyond the scope of this answer, but you can find the man page here.

