import sys, threading

def run():
    print("I'm thread %s" % threading.current_thread())

def main():
    print("I'm thread %s" % threading.current_thread())
    t = threading.Thread(target=run)
    t.start()

if __name__ == '__main__':
    main()
```

```
I'm thread <_MainThread(MainThread, started 140735194715776)>
I'm thread <Thread(Thread-1, started 123145559362304)>
```

**查看当前活动的线程数**
```python
import threading
import time

def run():
    time.sleep(3)

if __name__ == '__main__':
    print("Before:", threading.active_count())
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
    print("After:", threading.active_count())
```

```

