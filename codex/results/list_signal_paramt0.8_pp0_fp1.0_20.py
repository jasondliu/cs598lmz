import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print('DONE')
        sys.exit(1)

def main():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 1e-6)
    while True:
        pass

if __name__ == '__main__':
    main()
</code>
When I run this with CPython, this never exceeds 100% of one CPU core.
When I run this with PyPy, I see up to 500% CPU usage (5 stack switching events per second). I'm running on a Linux machine with 4 cores, but the CPU usage is exactly the same when I'm running it on a machine with 2 cores.
I've noticed that when I remove the <code>random.jumpahead(1)</code> call in <code>main()</code>, the CPU usage is reduced to about 200%. (But why does the CPU usage depend on the random seed?)
Looking at the code, <code>signal.setitimer</code> basically
