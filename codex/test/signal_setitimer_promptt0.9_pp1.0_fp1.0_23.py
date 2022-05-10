import signal
# Test signal.setitimer()
import signal
# signal.setitimer(signal.ITIMER_REAL, 1)
signal.setitimer(signal.ITIMER_VIRTUAL, 1)
# signal.setitimer(signal.ITIMER_PROF, 1)
signal.pause()
