import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        shutdown()
    return

def shutdown():
    print('complete')
    s.send_json({'_close_':True})
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

ctx = zmq.Context()
s = ctx.socket(zmq.PUSH)
s.connect("tcp://127.0.0.1:1234")
s.setsockopt(zmq.SNDHWM, 10)

i = 0
while (delays):
    i += 1
    s.send_json({'symbol':'GOOG', 'timestamp':time.time(), 'bid':100.0, 'ask':101.0, 'id':i, 'parent_id':0})
