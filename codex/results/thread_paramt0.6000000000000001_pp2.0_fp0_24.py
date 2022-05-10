import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('thread2\n')).start()
print('main')

# main
# thread2
# thread1

# thread1
# main
# thread2

# thread2
# main
# thread1

# main
# thread1
# thread2

```

```python
# 2.
import sys, threading
def f():
    sys.stdout.write('thread\n')
threading.Thread(target=f).start()
print('main')

# main
# thread

# thread
# main

# main
# thread

# thread
# main
```

```python
# 3.
import sys, threading
class MyThread(threading.Thread):
    def run(self):
        sys.stdout.write('thread\n')
MyThread().start()
print('main')

# main
# thread

# thread
# main

# main
# thread

