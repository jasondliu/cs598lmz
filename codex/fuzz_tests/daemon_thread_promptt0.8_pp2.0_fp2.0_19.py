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

print "Exiting main"

#Spawn a thread to monitor a directory

urls = ['http://www.yahoo.com',
        'http://www.cnn.com',
        'http://www.python.org',
        'http://www.jython.org',
        'http://www.pypy.org',
        'http://www.perl.org',
        'http://
