import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.setitimer(signal.ITIMER_REAL, delays.pop(0), delays[0])
signal.signal(signal.SIGALRM, handler)

loop = asyncio.SelectorEventLoop()
asyncio.set_event_loop(loop)

start = time.time()
end = start + 1

while loop.is_running():
    t = time.time()
    if t > end:
        loop.stop()
    else:
        loop.run_until_complete(asyncio.sleep(end - t))
