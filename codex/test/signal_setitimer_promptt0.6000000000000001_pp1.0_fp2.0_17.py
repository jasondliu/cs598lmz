import signal
# Test signal.setitimer() on SIGALRM
signal.setitimer(signal.ITIMER_REAL, 0.9, 0.2)

# Test signal.setitimer() on SIGVTALRM
signal.setitimer(signal.ITIMER_VIRTUAL, 0.9, 0.2)

# Test signal.setitimer() on SIGPROF
signal.setitimer(signal.ITIMER_PROF, 0.9, 0.2)

print('Sleeping for 2.0 seconds')
time.sleep(2.0)
print('Done sleeping')
