import signal
# Test signal.setitimer()
def signal_handler(signum, frame):
  print signum, frame
  signal.setitimer(signal.ITIMER_REAL, 1)
signal.signal(signal.SIGALRM, signal_handler)
signal.setitimer(signal.ITIMER_REAL, 5)
# raise SystemExit(0)
signal.pause()
