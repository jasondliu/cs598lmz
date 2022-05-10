import threading
# Test threading daemon
def delayed_print():
    time.sleep(15)
    print "Hello world"

thread = threading.Thread(target=delayed_print)
thread.daemon = True
thread.start()


# NOTE(chris): This will not run, because we set the daemon to true
for x in range(0,5):
  print "x: %s" % x
  time.sleep(1)
