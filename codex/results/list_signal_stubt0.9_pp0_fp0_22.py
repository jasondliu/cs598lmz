import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print("Все задержки добавлены")


signal.signal(signal.SIGALRM, handler)
print("Добавление задержек началось...")
signal.setitimer(signal.ITIMER_REAL, delays.pop())
while delays:
    try:
        signal.pause()
    except KeyboardInterrupt:
        break
</code>
Разница в обработке ошибок и в обработке остатков задержек после прерываний (у второго
