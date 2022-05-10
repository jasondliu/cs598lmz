import signal
# Test signal.setitimer

def handler(sig, frame):
    print sig
    print frame

signal.signal(signal.SIGALRM, 
