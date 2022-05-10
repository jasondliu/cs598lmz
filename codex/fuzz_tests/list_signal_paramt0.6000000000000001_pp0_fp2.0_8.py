import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

loop = get_event_loop()

def new_task():
    task = loop.create_task(coro())
    task.add_done_callback(lambda t: loop.call_soon(new_task))

loop.call_soon(new_task)
loop.run_forever()
