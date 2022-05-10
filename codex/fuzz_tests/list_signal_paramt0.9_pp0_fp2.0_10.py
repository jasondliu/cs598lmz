import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print('handler(%s, %s)' % (signum, frame))
    else:
        print('sleep(1000)')
        time.sleep(1000)

def wakeup():
    signal.signal(signal.SIGALRM, handler)
    handler()

if __name__ == '__main__':
    wakeup()
    print('sleep(1)')
    time.sleep(1)
    print('sleep(1)')
    time.sleep(1)
