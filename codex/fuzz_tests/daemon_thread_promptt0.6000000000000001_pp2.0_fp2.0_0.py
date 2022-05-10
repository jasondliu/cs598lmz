import threading
# Test threading daemon with a long-running thread

def main():
    print('main: starting')
    daemon = threading.Thread(target=daemon_thread, name='daemon')
    daemon.setDaemon(True)
    daemon.start()
    print('main: sleeping')
    time.sleep(0.1)
    print('main: exiting')

def daemon_thread():
    print('daemon: starting')
    time.sleep(0.1)
    print('daemon: exiting')

if __name__ == '__main__':
    main()

```

```
$ python3 daemon_thread.py
main: starting
daemon: starting
main: sleeping
daemon: exiting
main: exiting

```

## Threading Example

```python
# threading_simple.py
import threading
import time

def worker():
    """thread worker function"""
    print('Worker')
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target
