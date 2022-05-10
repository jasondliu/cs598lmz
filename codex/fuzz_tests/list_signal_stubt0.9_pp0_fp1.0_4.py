import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def alarm(*args):
    pass
signal.signal(signal.SIGALRM, alarm) # Coroutine으로 작성한 코드가 SIGALRM 발생시 alarm 함수를 호출하도록 설정

signal.setitimer(signal.ITIMER_REAL, delays.pop())
async def loop():
    while delays:
        await asyncio.sleep(0.01)

loop().send(None)
