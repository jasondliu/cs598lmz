import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1e")).start()
```

## Challenge

```
import sys, threading

class ThreadingTest(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting " + self.name)
        sys.stdout.write("\x1e")

thread_count = int(input("how many threads = "))
threads = []
for i in range(thread_count):
    thread = ThreadingTest(i, "Thread-" + str(i))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print("Exiting Main Thread")
```

## Explanation

`import sys` imports the `sys` module.

`import threading` imports the `threading` module.

`threading.Thread(target=lambda: sys.std
