import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print('Next set to:', delay)
    else:
        print('Stop')
        signal.setitimer(signal.ITIMER_REAL, 0)
        #raise Exception('stop')


def loop():
    while True:
        time.sleep(1)


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    loop()
