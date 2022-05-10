import threading
# Test threading daemon
def only_read(listx):
    while True:
        print('%s is reading list %s' % (threading.current_thread().name, listx))
        time.sleep(5)
l = threading.Lock()
t1 = threading.Thread(target=only_read,args=([1,2,3],), name="Thread_1")
t2 = threading.Thread(target=only_read,args=([4,5,6],), name="Thread_2")
# The daemon thread terminates as soon as the main thread terminates.
t1.setDaemon(True)
t2.setDaemon(True)
# Start the thread
t1.start()
t2.start()
# Only the main thread is still working
time.sleep(10)
