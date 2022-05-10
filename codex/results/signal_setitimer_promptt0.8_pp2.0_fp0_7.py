import signal
# Test signal.setitimer() and signal.getitimer()
signals = [x for x in dir(signal) if x.startswith("SIG")]

print("sig:")
for sig in signals:
    print("  "+sig)

print("")
print("alarm:")
print("  ", signal.getitimer(signal.ITIMER_REAL))
print("  ", signal.getitimer(signal.ITIMER_VIRTUAL))
print("  ", signal.getitimer(signal.ITIMER_PROF))
print("  ", signal.getitimer(signal.ITIMER_REAL))

signal.setitimer(signal.ITIMER_PROF, 1, 1)

print("  ", signal.getitimer(signal.ITIMER_REAL))
print("  ", signal.getitimer(signal.ITIMER_VIRTUAL))
print("  ", signal.getitimer(signal.ITIMER_PROF))
print("  ", signal.getitimer(signal.IT
