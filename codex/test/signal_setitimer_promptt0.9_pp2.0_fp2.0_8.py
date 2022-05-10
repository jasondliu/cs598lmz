import signal
# Test signal.setitimer
def t1(sig, frame):
    print("Timeout!")

signal.signal(signal.SIGALRM, t1)
signal.setitimer(signal.ITIMER_REAL, 1)
sleep(2)
signal.setitimer(signal.ITIMER_REAL, 0)
# Expected output:
#
# Timeout!
# Timeout!

################################################################################
# Test signal.setitimer with a custom callback
def t2(frame):
    print("Timeout!")

signal.signal(signal.SIGALRM, t2)
signal.setitimer(signal.ITIMER_REAL, 1)
sleep(2)
signal.setitimer(signal.ITIMER_REAL, 0)
# Expected output:
#
# Timeout!
# Timeout!

################################################################################
# Test signal.setitimer with cancellations
count = 0
def t3(sig, frame):
    global count
    count += 1
