import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0) # Disable timer
        print('Done')

def set_timer():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())

if __name__ == '__main__':
    set_timer()
    print('Waiting for {:0.5f} s'.format(sum(delays)))
    while(delays):
        signal.pause()
