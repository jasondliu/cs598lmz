import threading
# Test threading daemon

def hello():
    print "Hello"
    time.sleep(5)
    print "World"

t = threading.Thread(target=hello)
t.daemon = True
t.start()

print "Done"

# Test threading with lock

lock = threading.Lock()

def hello():
    with lock:
        print "Hello"
        time.sleep(5)
        print "World"

t = threading.Thread(target=hello)
t.start()

print "Done"

# Test threading with lock and daemon

lock = threading.Lock()

def hello():
    with lock:
        print "Hello"
        time.sleep(5)
        print "World"

t = threading.Thread(target=hello)
t.daemon = True
t.start()

print "Done"

# Test threading with lock and daemon and join

lock = threading.Lock()

def hello():
    with lock:
        print "Hello"
        time.sleep(5)
        print "
