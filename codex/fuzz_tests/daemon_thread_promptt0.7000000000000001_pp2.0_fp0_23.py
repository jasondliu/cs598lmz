import threading
# Test threading daemon
def test():
  while 1:
    print("test")
    time.sleep(1)

thread = threading.Thread(target=test)
thread.daemon = True
thread.start()

# Main program
while 1:
  print("Hello")
  time.sleep(1)
</code>

