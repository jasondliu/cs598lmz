import threading
# Test threading daemon
# This example demonstrates how to create threading.Timer objects
# The wait() method blocks until the thread terminates.
#

def hello():
    print('Hello, world!')

t = threading.Timer(5.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed
print("waiting")
t.join()
print("done")
