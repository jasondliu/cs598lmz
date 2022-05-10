import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 1.0, 1.0)
try:
  signal.setitimer(signal.ITIMER_VIRTUAL, 1.0, 1.0)
except AttributeError:
  pass
try:
  signal.setitimer(signal.ITIMER_PROF, 1.0, 1.0)
except AttributeError:
  pass

signal.alarm(1)
try:
  signal.setitimer(signal.ITIMER_REAL, 1.0, None)
except TypeError:
  pass
try:
  signal.setitimer(signal.ITIMER_REAL, None, None)
except TypeError:
  pass

try:
  signal.setitimer(signal.ITIMER_REAL, 1.0, -1.0)
except ValueError:
  pass
