import signal
# Test signal.setitimer()
def setitimer_handler(signum, frame):
    print('setitimer_handler')

signal.signal(signal.SIGALRM, setitimer_handler)
signal.setitimer(signal.ITIMER_REAL, 2, 1)
while True:
    print('while loop')
    time.sleep(1)

# Test signal.siginterrupt()
# def siginterrupt_handler(signum, frame):
#     print('siginterrupt_handler')
#
# signal.signal(signal.SIGINT, siginterrupt_handler)
# signal.siginterrupt(signal.SIGINT, True)
# while True:
#     print('while loop')
#     time.sleep(1)
