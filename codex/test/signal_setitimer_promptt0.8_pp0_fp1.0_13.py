import signal
# Test signal.setitimer()
#
# Usage: python signal_setitimer_test.py

class SetitimerTest:
  def __init__(self):
    signal.signal(signal.SIGALRM, self.handle_signal)

