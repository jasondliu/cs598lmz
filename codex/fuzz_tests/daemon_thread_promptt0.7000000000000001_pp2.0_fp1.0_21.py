import threading
# Test threading daemon
import time

# daemon thread is a background thread that is started by another thread.
# daemon thread terminates automatically when parent thread completes execution
# daemon thread cannot be terminated forcefully using join() method.
# daemon thread cannot create another thread.
# daemon thread do not wait for task to be completed.
# daemon thread is a low priority thread.
# daemon thread is used for background tasks like garbage collection, logging, monitoring

def sleep_thread():
    for i in range(1,5):
        print(i)
        time.sleep(1)

def sleep_thread2():
    for i in range(1,5):
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=sleep_thread)
t1.start()
print(t1.isDaemon())
#t1.setDaemon(True)
print(t1.isDaemon())
t2 = threading.Thread(target=sleep_thread2)
t2.start()
print(t2.isDaemon())
t2.setDaemon(True)
print(t
