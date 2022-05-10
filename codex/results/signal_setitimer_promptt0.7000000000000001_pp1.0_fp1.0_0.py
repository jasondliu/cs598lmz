import signal
# Test signal.setitimer

def handler(sig, frame):
    print "signal", sig
    print "frame", frame
    if frame:
        print "f_code", frame.f_code

def test():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 1, 0)
    for i in range(4):
        print i
        time.sleep(1)

test()
