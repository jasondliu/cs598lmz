import threading
# Test threading daemon

def say_hello():
    print "hello"
    t = threading.Timer(3, say_hello)
    t.start()

say_hello()
