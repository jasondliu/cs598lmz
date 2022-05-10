import signal
# Test signal.setitimer
def hdl(a, b):
    raise BaseException
signal.signal(signal.SIGALRM, hdl)
signal.setitimer(sig
