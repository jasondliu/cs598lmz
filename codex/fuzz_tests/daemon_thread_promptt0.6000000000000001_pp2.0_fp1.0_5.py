import threading
# Test threading daemon
# If the main thread is over, then the daemon thread will be killed
# 如果主线程结束，则守护线程也会结束
def func():
    print('func')
    time.sleep(2)
    print('func end')

t = threading.Thread(target=func)
t.setDaemon(True)
t.start()
print('main thread')
