import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        delay = delays.pop(0)
        print('.', end='', flush=True)
        time.sleep(random.random() * delay)
    else:
        print()
        print('Done.')
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# from https://stackoverflow.com/a/14104439/
