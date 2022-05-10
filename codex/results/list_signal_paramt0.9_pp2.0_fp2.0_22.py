import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays[0])
        delays.pop(0)

def emitter(q):
    for i in range(N):
        q.put(i)
    q.put(None)

def consumer(q):
    while delays:
        item = q.get()
        # print(len(q), item)
        if item is None:
            return

q = multiprocessing.Queue()
signal.setitimer(signal.ITIMER_REAL, delays[0])
delays.pop(0)

sig_thread = threading.Thread(target=signal.pause)
sig_thread.daemon = True
sig_thread.start()
signal.signal(signal.SIGALRM, handler)

thread = threading.Thread(target=emitter, args=(q,))
thread.daemon = True
thread.start()
consumer(q)
