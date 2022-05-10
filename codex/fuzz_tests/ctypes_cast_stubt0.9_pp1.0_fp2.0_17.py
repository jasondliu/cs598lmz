import ctypes
ctypes.cast(mythread.ident, ctypes.py_object).value = VALUE
```

Although you need to be careful not to create circular references.

<a name="markdown-how-do-i-use-the-threading-module" href="#how-do-i-use-the-threading-module">#</a> How do I use the `threading` module?
  
* Counter

      ```python
      import threading

      class Counter(object):
          def __init__(self):
              self.count = 0
              self.lock = threading.Lock()

          def increment(self, offset):
              with self.lock:
                  self.count += offset

      def worker(sensor_index, how_many, counter):
          for _ in range(how_many):
              # assumes a lock is held here
              counter.increment(1)

      def run_threads(func, how_many, counter):
          threads = []
          for i in range(5):
              args = (i, how_many, counter)
              thread = threading
