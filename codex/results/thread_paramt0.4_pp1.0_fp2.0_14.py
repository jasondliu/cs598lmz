import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Python 2.7
import thread
thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 1\n'), ())
thread.start_new_thread(lambda: sys.stdout.write('Hello from thread 2\n'), ())
```

## `threading.Thread`
```python
# Python 3
import threading
def worker():
    print('Hello from thread')
t = threading.Thread(target=worker)
t.start()
t.join()

# Python 2.7
import threading
def worker():
    print('Hello from thread')
t = threading.Thread(target=worker)
t.start()
t.join()
```

## `threading.Thread` with arguments
```python
# Python 3
import threading
def worker(num):
    print('Hello from thread {}'.format(num))

