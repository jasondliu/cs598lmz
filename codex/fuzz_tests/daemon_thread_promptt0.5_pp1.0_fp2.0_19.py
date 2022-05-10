import threading
# Test threading daemon

def my_function(i):
    print("sleeping 5 seconds from thread %d" % i)
    time.sleep(5)
    print("finished sleeping from thread %d" % i)

# spawn a thread
for i in range(10):
    t = threading.Thread(target=my_function, args=(i,))
    t.setDaemon(True)
    t.start()

print("done!")

# Test threading daemon

def my_function(i):
    print("sleeping 5 seconds from thread %d" % i)
    time.sleep(5)
    print("finished sleeping from thread %d" % i)

# spawn a thread
for i in range(10):
    t = threading.Thread(target=my_function, args=(i,))
    t.setDaemon(True)
    t.start()

print("done!")
