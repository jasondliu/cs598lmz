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

# The constructor takes a callable object and, optionally, a name for the thread.
# The callable object is usually a function, but it can be any callable object.
# The callable object is called the target of the thread.

# The run() method is the entry point for a thread.
# It must be overridden in a subclass.
# The run() method is called automatically when the thread begins.

# The start() method is called to start
