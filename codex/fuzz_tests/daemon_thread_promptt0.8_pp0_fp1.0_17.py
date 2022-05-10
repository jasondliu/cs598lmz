import threading
# Test threading daemon
f = daemon_t.Foo()
f.start()
print 'Main thread:', f, threading.currentThread()
del f
# Test threading non daemon
f = non_daemon_t.Foo()
f.start()
print 'Main thread:', f, threading.currentThread()
del f

print "DONE!"
