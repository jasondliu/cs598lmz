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
# The start() method starts a thread by calling the callable object passed to the object’s constructor as the target argument,
# if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.
# The join() method blocks the calling thread until the thread whose join() method is called is terminated.
# This blocks the main thread from exiting until all threads have exited.

# The threading module also provides a current_thread() function that returns the current thread and a
# enumerate() function that returns a list of all threads currently active.

# The threading module also provides a Lock class that can be used to synchronize threads.
# A lock has two states: locked and unlocked. It starts in the unlocked state.
# The acquire()
