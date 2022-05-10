import sys, threading

def run():
    print("Hello from new thread")

t = threading.Thread(target=run)
t.start()

print("Hello from main thread")

# Hello from main thread
# Hello from new thread

# The main thread creates a new thread and waits for it to finish.
# The new thread runs the function run() which prints a message.

# The threading module provides a Thread class to manage and run your threads.
# The Thread class represents an activity that is run in a separate thread of control.
# There are two ways to specify the activity: by passing a callable object to the constructor,
# or by overriding the run() method in a subclass.

# The constructor takes a callable object and, optionally, a name and a list of arguments.
# The callable object can be a function or a bound method.
# If the callable object is a function, the arguments are passed as a tuple.
# If the callable object is a bound method, the first argument is the instance,
# and the remaining arguments are passed as a tuple.

# The run() method is invoked by the start() method.
# The
