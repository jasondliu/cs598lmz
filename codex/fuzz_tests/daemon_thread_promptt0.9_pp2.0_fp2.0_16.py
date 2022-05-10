import threading
# Test threading daemon and join
def worker():
    print(threading.current_thread().getName(),'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(),'Exiting')

def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(3)
    print(threading.current_thread().getName(), 'Exiting')

t = threading.Thread(name='my_service',target=my_service)
w = threading.Thread(name='worker',target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()
# main thread waits for other threads to finish
# join() method blocks until the thread exits
w.join()
w2.join()
t.join()
# output:
# worker Starting
# worker Exiting
# Thread-7 Starting
# worker Starting
# worker Exiting
# my_service Starting
# my_service Exiting
# When threads start with join(), default is false
#
