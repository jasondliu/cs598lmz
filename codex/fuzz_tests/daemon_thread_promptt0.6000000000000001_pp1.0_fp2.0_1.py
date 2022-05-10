import threading
# Test threading daemon
def worker():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(0.2)
    print(threading.currentThread().getName(),'Exiting')
    
def my_service():
    print(threading.currentThread().getName(),'Starting')
    time.sleep(0.3)
    print(threading.currentThread().getName(),'Exiting')
    
t = threading.Thread(name='my_service',target=my_service)
w = threading.Thread(name='worker',target=worker)
w2 = threading.Thread(target=worker)
w.start()
w2.start()
t.start()

# Set daemon to True, then main thread exit and daemon thread will exit too.
# Otherwise, daemon thread will not exit until main thread exit.
t.setDaemon(True)

print(w.getName(),'Daemon:',w.isDaemon())
print(t.getName(),'Daemon:',t.isDaemon())

print(w2.getName(),
