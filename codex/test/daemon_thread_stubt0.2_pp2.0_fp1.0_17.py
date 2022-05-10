import sys, threading

def run():
    print("Hello from new thread")

t = threading.Thread(target=run)
t.start()

print("Hello from main thread")

# Hello from main thread
# Hello from new thread

# The threading module provides a Thread class to manage and run your threads.
# The target argument is the callable object to be invoked by the run() method.
# The start() method starts a thread by calling the callable object passed to the object.
# The join() method waits for the thread to terminate.

# The threading module also provides a current_thread() function that returns the current thread and a enumerate() function that returns a list of all threads currently active.

# The threading module also provides Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Timer and Barrier classes to handle synchronization between threads.

# The queue module provides a Queue class that is especially useful for coordinating work between threads.

# The multiprocessing module provides a Process class that is similar to the Thread class.
# The multiprocessing module also provides a Pool class that can be used to manage a
