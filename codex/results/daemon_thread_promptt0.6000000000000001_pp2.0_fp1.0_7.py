import threading
# Test threading daemon
class MyThread(threading.Thread):
    def run(self):
        global n
        lock.acquire()
        temp = n
        time.sleep(0.001)
        n = temp - 1
        lock.release()

lock = threading.Lock()
n = 100
thread_list = []
for i in range(100):
    t = MyThread()
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

if n == 0:
    print('success')
else:
    print('failed')

# Test threading lock
lock = threading.Lock()
n = 100

def func():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.001)
    n = temp - 1
    lock.release()

thread_list = []
for i in range(100):
    t = threading.Thread(target=func)
    t.start()
    thread_list.append(t)

for t in thread
