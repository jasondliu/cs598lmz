import signal
# Test signal.setitimer() here and there
def signal_handler(signal, frame):
  print("Signal handler for signal {}".format(signal))

signal.signal(signal.SIGVTALRM, signal_handler)
signal.signal(signal.SIGALRM, signal_handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
#time.sleep(10)

signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
#time.sleep(10)

signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
#time.sleep(10)

signal.alarm(3)

if __name__ == "__main__":
  print("Will sleep 10 seconds")
  time.sleep(10)
  print("Done 1")
