import signal
# Test signal.setitimer
def handler(signum, frame):
    print("handler is invoked")
    signal.setitimer(signal.ITIMER_REAL, 0.5)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5)

while True:
    pass

# Test signal.getsignal
#def handler(signum, frame):
#    print("handler is invoked")
#
#signal.signal(signal.SIGALRM, handler)
#print(signal.getsignal(signal.SIGALRM))
#print(signal.getsignal(signal.SIGINT))
#print(signal.getsignal(signal.SIGQUIT))
#print(signal.getsignal(signal.SIGABRT))
#
#while True:
#    pass
# Test signal.getitimer
# def handler(signum, frame):
#    print("handler is invoked")
#    signal.setitimer
