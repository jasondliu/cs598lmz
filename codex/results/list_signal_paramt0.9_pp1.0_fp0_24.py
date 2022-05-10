import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, random.choice(delays))
    else:
        print "Done!"
        exit(0)
        
signal.signal(signal.SIGALRM, handler)

# kick it off
signal.setitimer(signal.ITIMER_REAL, random.choice(delays))

while True:
    time.sleep(1)
