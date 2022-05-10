import threading
# Test threading daemon

def thread_func(name):
    print "thread %s is running..." % name
    time.sleep(1)
    print "thread %s is over..." % name

print "main thread is running..."
t = threading.Thread(target=thread_func, args=('test',))
#t.setDaemon(True)
t.start()
#t.join()
print "main thread is over..."
