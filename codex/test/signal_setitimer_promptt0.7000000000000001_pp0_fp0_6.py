import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
# Several seconds later
time.sleep(2)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
# Several seconds later
time.sleep(2)
# The timer is canceled
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
