import signal
# Test signal.setitimer
# Expecting:
#   setitimer(ITIMER_VIRTUAL, 0.1, 0.2)
#   sleep(0.3)
#   setitimer(ITIMER_VIRTUAL, 0, 0)
#   sleep(0.4)

def alarm_handler(sig, arg):
    pass

signal.signal(signal.SIGALRM, alarm_handler)

signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.2)
time.sleep(0.3)
signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
time.sleep(0.4)
