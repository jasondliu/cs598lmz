import signal
# Test signal.setitimer() in ctrl-c handler
def setitimer_test():
    import os
    import signal
    global called_handler
    def alarm_handler(signum, frame):
        global called_handler
        if 'called' in called_handler:
            called_handler['alarm'] = True
            global n
            n += 1
        else:
            sig = signal.getsignal(signal.SIGALRM)
            signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
            signal.signal(signal.SIGALRM, sig)
            called_handler['called'] = True
    def keyb_handler(signum, frame):
        global called_handler
        if 'called' in called_handler:
            called_handler['keyb'] = True
