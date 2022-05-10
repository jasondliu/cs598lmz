import signal
# Test signal.setitimer()
#
def handler(signum, frame):
    print("in handler")
    time.sleep(3)
    print("out handler")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 2, 0)

while True:
    print("not in handler")
    time.sleep(1)


#
# Test signal.setitimer()
#
def handler(signum, frame):
    print("in handler")
    time.sleep(3)
    print("out handler")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 2, 0)

while True:
    print("not in handler")
    time.sleep(1)



# 
# Test signal.setitimer()
#
def handler(signum, frame):
    print("in handler")
    time.sleep(3)
    print("out handler")

signal.sign
