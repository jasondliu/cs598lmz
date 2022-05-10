import threading
# Test threading daemon
import threading
import time

def worker(interval):
    print("worker start")
    print(threading.current_thread())
    time.sleep(interval)
    print("worker end")

print(threading.current_thread())
t = threading.Thread(target=worker, args=(5,))
t.setDaemon(True) # 将此线程设置为守护线程
t.start()
t.join()
print("main thread end")

# Test threading join
import threading
import time

def worker():
    print(threading.current_thread())
    time.sleep(2)
    print("worker")

t = threading.Thread(target=worker, args=())
t.start()
t.join()
print(threading.current_thread())
print("main thread end")

# Test threading lock
import threading
import time

total = 0
lock = threading.Lock()
def add():
    global total
