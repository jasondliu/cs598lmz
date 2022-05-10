import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        IOLoop.instance().stop()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

def periodic():
    print "periodic in thread"

@gen.engine
def periodic_yielded(callback):
    print "periodic in thread"
    callback()

if __name__ == "__main__":
    IOLoop.instance().add_timeout(time.time(), periodic)
    PeriodicCallback(periodic, 1000, IOLoop.instance()).start()
    PeriodicCallback(partial(periodic_yielded, IOLoop.instance().stop), 1000, IOLoop.instance()).start()
    main = IOLoop.instance().start
