import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("now I have to do something")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5, 0)

while True:
    print("doing something in a loop ...")
    time.sleep(2)

print("done")
