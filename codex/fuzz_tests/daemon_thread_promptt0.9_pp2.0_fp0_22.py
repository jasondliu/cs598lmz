import threading
# Test threading daemon
def f():
    print 'thread function'
    return
 
threadex = threading.Thread(target=f)
threadex.setDaemon(True)  # comment this line and see what happens
threadex.start()
threadex.join()

#
