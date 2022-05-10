import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def main():
    signal.signal(signal.SIGALRM, handler)

    signal.setitimer(signal.ITIMER_REAL, delays.pop())

    while delays:
        time.sleep(2)

if __name__ == "__main__":
    main()
</code>


A:

Можно поступить так:
<code>import signal
import time
import random
import queue

def handler(signum, frame):
    pass

def sched():
    signal.signal(signal.SIGHUP, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5) # последовательность вызовов
    for i in range(5):
        signal.pause() # ждем сигнала
        print('Запускаем 
