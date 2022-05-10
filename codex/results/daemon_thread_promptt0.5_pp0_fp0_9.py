import threading
# Test threading daemon
#def func():
#    print 'func() passed to threading.Thread'

#t = threading.Thread(target=func)
#t.setDaemon(True)
#t.start()
#t.join()

# Test python daemon
#def func():
#    print 'func() passed to threading.Thread'

#t = threading.Thread(target=func)
#t.start()
#t.join()

# Test python daemon
#def func():
#    print 'func() passed to threading.Thread'

#t = threading.Thread(target=func)
#t.start()
#t.join()

# Test python daemon
def func():
    print 'func() passed to threading.Thread'

t = threading.Thread(target=func)
t.start()
t.join()
