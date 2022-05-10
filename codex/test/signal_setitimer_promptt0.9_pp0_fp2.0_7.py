import signal
# Test signal.setitimer/getitimer
for timer in ['ITIMER_REAL', 'ITIMER_VIRTUAL', 'ITIMER_PROF']:
    print(timer, ':', end=' ')
    print(signal.getitimer(eval('signal.%s' % timer)))
# Test signal.signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
print('SIGALRM ignored:', end=' ')
print(signal.getsignal(signal.SIGALRM) == signal.SIG_DFL)
# Pass a callable as a handler
signal.signal(signal.SIGINT, lambda x, y: None)

def handler(signum, frame):
    pass

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGINT, signal.SIG_IGN)
# Check that exceptions in the handler are caught
def cause_exception(signum, frame):
    raise RuntimeError('exception in signal handler')

