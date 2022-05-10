import threading
# Test threading daemonic
def daemon():
    print('Starting:', threading.current_thread().name)
    time.sleep(2)
    print('Exiting :', threading.current_thread().name)
d = threading.Thread(name='daemon', target=daemon, daemon=True)
d.start()

def non_daemon():
    print('Starting:', threading.current_thread().name)
    print('Exiting :', threading.current_thread().name)
t = threading.Thread(name='non-daemon', target=non_daemon)
t.start()

# Test result
'''
    Starting: non-daemon
    Starting: daemon
    Exiting : non-daemon
'''
```

**Daemon and non-daemon threads**

Main threads, by default, are non-daemon threads. Main threads create other threads. Daemon threads are terminated automatically when all the non-daemon threads have completed their execution.

If there is any non-daemon thread still active, the program keeps running even if all daemon threads have completed execution.
