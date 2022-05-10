import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# 2: If you need to wait until the thread has terminated, call join() on it.
def hello():
    sys.stdout.write('Hello World\n')

t = threading.Thread(target=hello)
t.start()
t.join()

# 3: Use a subclass of Thread to define a new thread type. Override __init__()
# and run().
class HelloWorld(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        sys.stdout.write('Hello World\n')

HelloWorld().start()

# 4: If your thread performs a blocking operation (like I/O), tell Python to
# release the GIL while it is blocked by calling the lock type's acquire()
# method and release() method, as documented in the "reference" documentation.
# This allows other threads to run in parallel.
import select

def hello():
    select.select([
