import signal
# Test signal.setitimer()
def handler(signum, frame):
  print("Tick")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
  signal.pause()

# Test signal.setitimer() with a single-shot timer
def handler(signum, frame):
  print("Tick")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

while True:
  signal.pause()

# Test signal.setitimer() with a periodic timer
def handler(signum, frame):
  print("Tick")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0, 0.1)

while True:
  signal.pause()

# Test signal.setitimer() with a periodic timer, then
