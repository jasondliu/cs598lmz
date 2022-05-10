import signal
# Test signal.setitimer()
def handler(signum, frame):
    print('Alarm!')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 3)

while True:
    print('Tick!')
    time.sleep(1)

# Test signal.setitimer()
# def handler(signum, frame):
#     print('Alarm!')

# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_REAL, 3)

# while True:
#     print('Tick!')
#     time.sleep(1)

# Test signal.setitimer()
# def handler(signum, frame):
#     print('Alarm!')

# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_REAL, 3)

# while True:
#     print('Tick!')
#     time.sleep
