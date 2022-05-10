import signal
# Test signal.setitimer()
def handler(signum, frame):
    print("get signal")
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)
while True:
    print("process")
    time.sleep(1)

signal.alarm(5)
signal.signal(signal.SIGALRM, handler)

while True:
    print('process')
    time.sleep(1)

# Test signal.signal()
signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    print("process")
    time.sleep(1)

signal.signal(signal.SIGINT, signal.SIG_DFL)
while True:
    print("process")
    time.sleep(1)

# Test signal.getsignal()
print(signal.getsignal(signal.SIGINT))

def handler(signum, frame):
    print("got signal:",
