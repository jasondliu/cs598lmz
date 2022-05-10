import signal
# Test signal.setitimer
signal.signal(signal.SIGALRM, lambda x,y: None)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
import time
time.sleep(1)
