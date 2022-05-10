import threading
# Test threading daemon
# 主线程结束，子线程也结束
def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(0.2)
    print(threading.currentThread().getName(),'Exiting')

def my_service():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(0.3)
    print(threading.currentThread().getName(),'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
