import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

def x():
    signal.signal(signal.SIGALRM, handler)
    handler()
    while True:
        pass

def main():
    multiprocessing.set_start_method('fork', force=True)
    pool = multiprocessing.Pool(1)
    pool.apply(x)
    pool.close()
    pool.join()

main()
 
</code>

