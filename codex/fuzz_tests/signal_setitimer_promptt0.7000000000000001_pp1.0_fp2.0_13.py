import signal
# Test signal.setitimer() and signal.getitimer()
def sig_usr(signo, frame):
    print 'receive', signo
    if signo == signal.SIGALRM:
        print 'SIGALRM'
    elif signo == signal.SIGVTALRM:
        print 'SIGVTALRM'
    else:
        print 'unknown'
    print 'getitimer():', signal.getitimer(signo)

signal.signal(signal.SIGALRM, sig_usr)
signal.signal(signal.SIGVTALRM, sig_usr)

print 'setitimer():', signal.setitimer(signal.SIGALRM, 1, 1)
print 'setitimer():', signal.setitimer(signal.SIGVTALRM, 2, 2)

signal.pause()
