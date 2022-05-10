import threading
# Test threading daemon
event = threading.Event()

def f():
 print('thread function')
 t = threading.currentThread()
 x = 0
 while not event.isSet():
  x = x + 1
 print('thread ended')

thread = threading.Thread(target=f)
thread.start()
print('Main thread')
thread.join(timeout=1.0)
print('Main thread waiting ended')
x = threading.activeCount()
print('active thread count:', x)

print('stopping thread')
event.set()
thread.join()
print('thread stopped')

print('stopped')
