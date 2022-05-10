import signal
signal.signal(signal.SIGINT, exit_handler)

while True:
  print "lmao"
