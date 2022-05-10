import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("End of delays.")
        signal.setitimer(signal.ITIMER_REAL, 0)
    return

signal.signal(signal.SIGALRM, handler)
handler()

print("Starting loop.")

i = 1000000
while i:
    i -= 1
    """
    아래의 code는 signal.signal을 통해 설정하는 것과 
    동일한 동작을 하는 코드이며, 해당 코드 안에서의 시그널의 처리는 비동기적으로 처리된다
    """
    signal.setit
