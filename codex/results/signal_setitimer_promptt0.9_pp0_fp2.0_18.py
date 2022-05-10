import signal
# Test signal.setitimer
print(signal.setitimer(signal.ITIMER_REAL, 0.4))
print(signal.setitimer(signal.ITIMER_VIRTUAL, 0.5, 0.6))
print(signal.setitimer(signal.ITIMER_PROF, 0.8, 0.9))
# Test signal.getitimer
print(signal.getitimer(signal.ITIMER_REAL))
print(signal.getitimer(signal.ITIMER_VIRTUAL))
print(signal.getitimer(signal.ITIMER_PROF))

print(signal.setitimer(signal.ITIMER_REAL, 0))
