import threading
# Test threading daemoning
import time
import heapq as _heapq

# A timer class for every object, every function
class Timer:
  def __init__(self, interval, function, args=[], kwargs={}):
    self.time_created = time.time()
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.thread = threading.Thread(target=self.run, args=self.args, kwargs=self.kwargs)
    self.thread.daemon = True
  def run(self):
    self.start_time = time.time()
    while True:
      if self.start_time < time.time() - self.interval:
        self.function(*self.args, **self.kwargs)
        self.start_time = time.time()
  def cancel(self):
    pass

class PeriodicTimer:
  # Will call the function every interval secs.
  # If the function takes too long, it is called again anyway.
 
