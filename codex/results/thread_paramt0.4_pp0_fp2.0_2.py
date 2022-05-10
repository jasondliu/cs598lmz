import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread\n")).start()

# The threading.Thread class is a subclass of the threading.Thread class.
# The constructor for Thread takes a callable object and, optionally, a name.
# The callable object is called the target of the thread.

# When the thread is started, the run() method of the target is invoked in a separate thread of control.
# The target is passed to the constructor of the Thread class as its first argument.
# The optional name argument is the thread name.
# If not specified, the name of the thread defaults to “Thread-N”, where N is a small decimal number.

# The start() method of the Thread class invokes the run() method of the target in a separate thread of control.
# The join() method of the Thread class waits for the thread to terminate.
# The is_alive() method of the Thread class returns True if the thread is still running and False otherwise.

# The threading module also defines a current_thread() function that returns the Thread object for the current thread.
# The getName() method of the Thread
