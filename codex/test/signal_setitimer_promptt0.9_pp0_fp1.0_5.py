import signal
# Test signal.setitimer()

def handler(signum, frame):
    print ("In handler")

signal.signal(signal.SIGALRM, handler)

interval = 5
signal.setitimer(signal.ITIMER_REAL, interval)

while True:
    signal.pause()
