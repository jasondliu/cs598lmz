import threading
# Test threading daemon

class TestThreading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for x in range(0,100):
            print x
            time.sleep(1)

if __name__ == '__main__':
    test_thread = TestThreading()
    test_thread.start()
    test_thread.join(timeout=30)
    print "done"

```

### Threading with queue
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import threading
import Queue

class TestThreading(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            print self.queue.get()
            self.queue.task_done()

if __name__ == '__main__':
    queue = Queue.Queue()
   
