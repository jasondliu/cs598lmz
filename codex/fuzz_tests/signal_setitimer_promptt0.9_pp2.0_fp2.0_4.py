import signal
# Test signal.setitimer()
from time import sleep

def test_timer(count):
  """
  Test signal.setitimer()
  """
  def catch_timer(signum, stackframe):
    print "hello, timer num: ", count
  
  # Register a signal handler
  signal.signal(signal.SIGALRM, catch_timer)
  
  # Define an interval timer (3 sec)
  signal.setitimer(signal.ITIMER_REAL, 3, 0)

if __name__ == "__main__":
  print "start"
  test_timer(1)
  test_timer(2)
  test_timer(3)
  
  print "sleeping"
  sleep(20)
  print "goodbye"
