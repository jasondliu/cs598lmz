import signal
# Test signal.setitimer() function

SIGALRM = signal.SIGALRM
SIGVTALRM = signal.SIGVTALRM

def alarm_handler(sig, sf):
    print("sig %d, sf %s" % (sig, sf))

signal.signal(SIGALRM, alarm_handler)
signal.signal(SIGVTALRM, alarm_handler)

signal.setitimer(SIGALRM, 3)
signal.setitimer(SIGVTALRM, 2, 1)

try:
    print("starting sleep")
    time.sleep(10)
    print("ended sleep")
except:
    print("got exception while sleeping")
    pass

