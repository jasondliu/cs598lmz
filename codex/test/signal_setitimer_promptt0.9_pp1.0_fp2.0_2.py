import signal
# Test signal.setitimer() to raise a signal upon expiry:
timeout_seconds = 0.5
def handler(signum, frame):
  print('Expired by {}'.format(signum))
  raise TimeoutError("Error timeout exceeded")
signal.signal(signal.SIGPROF, handler)
signal.setitimer(signal.ITIMER_PROF, timeout_seconds)
try:
  while True:
    pass
except TimeoutError as e:
  pass
signal.setitimer(signal.ITIMER_PROF, 0)  # Disarm itimer
print('')
print('============================================================')
print('============================================================')
print('============================================================')
print('========================SETITIMER===========================')
print('============================================================')
print('============================================================')
print('============================================================')
print('')

print('=======================SIGNAL================================')
print('============================================================')
print('============================================================')
print('============================================================')
print('')
import signal
# Test signal.SIGALRM, raise a signal
