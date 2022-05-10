import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# Test signal.getitimer
print signal.getitimer(signal.ITIMER_REAL)
# Test signal.alarm
signal.alarm(1)
# Test signal.signal
signal.signal(signal.SIGINT, signal.SIG_IGN)
# Test signal.getsignal
print signal.getsignal(signal.SIGINT)
# Test signal.pause
signal.pause()

# Test some signals
for i, sig in enumerate(dir(signal)):
    if sig.startswith("SIG") and not sig.startswith("SIG_"):
        name = sig
        num = getattr(signal, sig)
        print name, num
        try:
            signal.signal(num, signal.SIG_IGN)
        except ValueError:
            print "signal.signal(%s) raised ValueError" % name
            continue
        try:
            signal.
