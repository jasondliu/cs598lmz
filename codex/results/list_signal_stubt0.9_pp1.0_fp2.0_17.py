import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
handler()

handlerdict = {}

def handlerfactory1(i):
    def handler(sig, frame):
        print(i)
        sys.exit(0)
    return handler

handlerdict[1] = handlerfactory1(1)
handlerdict[2] = handlerfactory1(2)
handlerdict[3] = handlerfactory1(3)
handlerdict[4] = handlerfactory1(4)
handlerdict[5] = handlerfactory1(5)
handlerdict[6] = handlerfactory1(6)
handlerdict[7] = handlerfactory1(7)
handlerdict[8] = handlerfactory1(8)
handlerdict[9] = handlerfactory1(9)

# handlerdict = {}
# handlerdict[1] = lambda sig, frame: print(1)
# handlerdict[2] = lambda sig, frame: print(2)
# handlerdict[3] = lambda sig
