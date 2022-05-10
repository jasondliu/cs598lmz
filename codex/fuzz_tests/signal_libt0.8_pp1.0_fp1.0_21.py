import signal
signal.signal(signal.SIGINT, SIGINT_handler)

for i in range(10):
  print("*")
  time.sleep(1)

print("Exiting program")
