import signal
# Test signal.setitimer value in seconds
time_to_wait=30
def my_custom_exception_handler(signal, frame):
  raise Exception("Time out!")

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, my_custom_exception_handler)
signal.setitimer(signal.ITIMER_REAL, time_to_wait)

print "Starting!"
try:
  while True:
    time.sleep(1)
    print ".",
except Exception, exc:
  print "Exception", exc
