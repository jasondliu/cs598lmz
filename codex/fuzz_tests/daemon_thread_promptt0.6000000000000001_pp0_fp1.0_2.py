import threading
# Test threading daemon mode
# The main thread exits and daemon thread is killed as well
# The daemon thread cannot be join()
def worker():
    print("I'm a thread")
    time.sleep(10)
    print("I'm done")

thread = threading.Thread(target=worker)
thread.daemon = True
thread.start()

print("Main thread exiting")

# Test threading join
# The main thread waits for the daemon thread to finish
# thread.join()

# Test threading lock
# Threads can use the lock to use the resource in an orderly fashion
# It will wait it's chance to use the resource
# It's common to use this lock in a with statement
lock = threading.Lock()
def worker():
    with lock:
        print("I'm a thread")
        time.sleep(10)
        print("I'm done")

thread = threading.Thread(target=worker)
thread.daemon = True
thread.start()

print("Main thread exiting")

# Test threading RLock
# Recursive lock. A thread can acquire the lock twice
#
