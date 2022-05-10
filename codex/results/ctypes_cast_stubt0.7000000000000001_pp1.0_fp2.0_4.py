import ctypes
ctypes.cast(ptr, ctypes.py_object).value

# Create a low-level lock object
lock = thread.allocate_lock()
lock.acquire()
lock.release()

# Locking support for shared state
x = 0
COUNT = 10**7

def add_python():
    global x
    for i in range(COUNT):
        x += 1
    print('%s: x = %i' % (threading.current_thread().name, x))

def add_threads():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=add_python)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return x

add_threads()

# The Global Interpreter Lock (GIL)
import subprocess
subprocess.call(['python', '-c', 'import threading; print(threading.current_thread().name)'])

# A threading example
import threading
def action(i):
    # Get
