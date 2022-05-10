import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Done')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.pause()
</code>
Код правильно работает ПОЧТИ, но существует существенная проблема: он блокирует потоки, даже если они не вызываются из сигнала. Например, при поиске в большом проекте
<code>while True:
    signal.pause()
