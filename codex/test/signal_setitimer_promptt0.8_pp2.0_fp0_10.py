import signal
# Test signal.setitimer()/signal.getitimer()
try:
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.3)
except:
    print("SKIP")
    raise SystemExit

def handler(signum, frame):
    print(signum)
    print(signum == signal.SIGVTALRM)
    print("signal received")

signal.signal(signal.SIGVTALRM, handler)

signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.3)
#check function return value
print(signal.setitimer(signal.ITIMER_VIRTUAL, 0.2, 0.3))
#check getitimer() return value after setitimer()
print(signal.getitimer(signal.ITIMER_VIRTUAL))
#check getitimer() return value after signal.setitimer(0)
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
