import threading
# Test threading daemon thread is really a daemon thread
def foo():
    print(threading.current_thread().getName())
    t = threading.Timer(2, foo)
    t.daemon = True
    t.start()

t = threading.Timer(2, foo)
t.daemon = True
t.start()
print(t.isDaemon())
time.sleep(10)
#print(threading.current_thread().getName())
#print(t.isDaemon())

# Test threading daemon thread is really a daemon thread
def foo1():
    print(threading.current_thread().getName())
    t = threading.Timer(2, foo1)
    t.daemon = False
    t.start()

t = threading.Timer(2, foo1)
t.daemon = False
t.start()
print(t.isDaemon())
time.sleep(10)
#print(threading.current_thread().getName())
#print(t.isDaemon())
