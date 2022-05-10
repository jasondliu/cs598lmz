import signal
# Test signal.setitimer and signal.getitimer

def handler(signum, frame):
    print("signal", signum)
    raise SystemExit

# Test with alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)

# Test with a virtual timer
signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 0)

# Test with a profiler timer
signal.signal(signal.SIGPROF, handler)
signal.setitimer(signal.ITIMER_PROF, 0.5, 0)

# Test getitimer
print(signal.getitimer(signal.ITIMER_REAL))
print(signal.getitimer(signal.ITIMER_VIRTUAL))
print(signal.getitimer(signal.ITIMER_PROF))

# Test setitimer with a
