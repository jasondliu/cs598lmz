import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 3\n')).start()

# A lock is required to prevent threads from writing to stdout at the same time
import threading, time
stdout_lock = threading.Lock()
def thread_function(name):
    with stdout_lock:
        print('Thread %s: starting' % name)
    time.sleep(2)
    with stdout_lock:
        print('Thread %s: finishing' % name)
x = threading.Thread(target=thread_function, args=(1,))
y = threading.Thread(target=thread_function, args=(2,))
x.start()
y.start()
x.join()
y.join()

# The threading module can also be used to create a thread that executes a
# function periodically, as in a timer
import threading

