import sys, threading

def run():
  t = threading.currentThread()
  while getattr(t, "do_run", True):
    sys.stdout.write("scheduling...\n")
    for i in range(1000000):
      pass
  sys.stdout.write("stopping\n")

thread = threading.Thread(target=run)
thread.start()

time.sleep(3)
thread.do_run = False
thread.join()

```

```python

>>> import scheduler
>>> import time

>>> scheduler.print_scheduler()
scheduler values (shared):
  a: 0
  b: 0

>>> scheduler.update_scheduler(a=1)

>>> scheduler.print_scheduler()
scheduler values (shared):
  a: 1
  b: 0

>>> time.sleep(3)

>>> scheduler.print_scheduler()
scheduler values (shared):
  a: 1
  b: 0

>>> scheduler.update_scheduler(a=2
