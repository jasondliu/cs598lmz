import threading
# Test threading daemon

def daemon():
    print 'Starting:', threading.currentThread().getName()
    time.sleep(2)
    print 'Exiting :', threading.currentThread().getName()

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print 'Starting:', threading.currentThread().getName()
    print 'Exiting :', threading.currentThread().getName()

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# http://stackoverflow.com/questions/190010/daemon-threads-explanation

# If you have a number of threads that need to run for the lifetime of the process, 
# you can simply set them as daemons and not bother with joining them. 
# If you have a number of threads that need to exit when the main thread exits, 
# you can use the join method to
