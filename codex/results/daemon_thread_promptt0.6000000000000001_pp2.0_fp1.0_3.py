import threading
# Test threading daemon
#def daemon():
#    print 'Starting:', threading.currentThread().getName()
#    time.sleep(2)
#    print 'Exiting :', threading.currentThread().getName()

#d = threading.Thread(name='daemon', target=daemon)
#d.setDaemon(True)

#def non_daemon():
#    print 'Starting:', threading.currentThread().getName()
#    print 'Exiting :', threading.currentThread().getName()

#t = threading.Thread(name='non-daemon', target=non_daemon)

#d.start()
#t.start()

#d.join()
#t.join()

# Test multiple threads
#def worker():
#    print threading.currentThread().getName(), 'Starting'
#    time.sleep(2)
#    print threading.currentThread().getName(), 'Exiting'

#def my_service():
#    print threading.currentThread().getName(), 'Starting'
#    time.sleep
