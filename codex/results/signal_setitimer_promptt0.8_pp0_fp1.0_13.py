import signal
# Test signal.setitimer()
#
# Usage: python signal_setitimer_test.py

class SetitimerTest:
  def __init__(self):
    signal.signal(signal.SIGALRM, self.handle_signal)

  def handle_signal(self, signum, frame):
    print signum, frame

def main():
  test = SetitimerTest()
  signal.setitimer(signal.ITIMER_REAL, 1, 1)
  counter = 100
  while counter:
    print counter
    counter -= 1

if __name__ == '__main__':
  main()
