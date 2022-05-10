import signal
# Test signal.setitimer()

def handler(signum, frame):
  print("Handler!")

print("Registering...")
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 3)
print("Registered!")


i = 0
while 1:
  #print("Tick")
  time.sleep(1)
  i += 1
  if i == 5:
    print("Trying to unregister...")
    signal.setitimer(signal.ITIMER_REAL, 0)
    print("Unregistered!")

print("End")
