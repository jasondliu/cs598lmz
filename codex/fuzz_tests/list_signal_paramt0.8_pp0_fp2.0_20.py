import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        sys.exit(0)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

lengths = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
counts = [0]*len(lengths)
while 1:
    for i in range(len(lengths)):
        count = 0
        for j in range(10000/N*lengths[i]):
            count += 1
            if j % lengths[i] == 0:
                counts[i] += 1
                #print i, counts[i], count
                break
    print counts
