import threading
# Test threading daemon

def func1():
    print "func1 start"
    time.sleep(3)
    print "func1 end"

def func2():
    print "func2 start"
    time.sleep(3)
    print "func2 end"

def func3():
    print "func3 start"
    time.sleep(3)
    print "func3 end"

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)

t1.daemon = True
t2.daemon = True
t3.daemon = True

t1.start()
t2.start()
t3.start()

print "main thread end"
