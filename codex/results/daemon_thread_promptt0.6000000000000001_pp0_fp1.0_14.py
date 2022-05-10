import threading
# Test threading daemon
# The program will exit even if the thread is still running

def worker():
  t = threading.currentThread()
  print("Thread {} is running".format(t.name))
  while getattr(t, "do_run", True):
    time.sleep(1)
  print("Thread {} is done".format(t.name))

t = threading.Thread(target=worker)
t.start()
time.sleep(5)
t.do_run = False
t.join()

# If you don't want the program to exit after the main thread is done,
# set the thread to daemon mode
t = threading.Thread(target=worker)
t.daemon = True
t.start()
time.sleep(5)
t.do_run = False
t.join()
