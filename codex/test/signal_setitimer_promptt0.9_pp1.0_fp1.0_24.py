import signal
# Test signal.setitimer(itimer, value) in signal handler

class TestSetitimer:
  def __init__(self):
    signal.signal(signal.SIGALRM, self.signal_handler)
    signal.signal(signal.SIGVTALRM, self.vt_signal_handler)

  def signal_handler(self, signum, frame):
    signal.alarm(1)  # reset it

  def vt_signal_handler(self, signum, frame):
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.2) # reset it
