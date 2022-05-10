import threading
# Test threading daemon
def func():
    print('sub thread')
    t = threading.currentThread()
    time.sleep(10)
    print('sub thread end')

t = threading.Thread(target=func)
t.setDaemon(True)
t.start()
print('sub thread is alive: %s' % t.is_alive())
print('main thread')
time.sleep(3)
print('main thread end')
