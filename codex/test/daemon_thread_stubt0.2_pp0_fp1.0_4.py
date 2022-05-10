import sys, threading

def run():
    print("Hello from new thread")

t = threading.Thread(target=run)
t.start()

print("Hello from main thread")

# Hello from main thread
# Hello from new thread

# The main thread creates a new thread and waits for it to finish.
# The new thread prints a message then terminates.

# The output is printed in an arbitrary order.
# The main thread might finish before the new thread starts.
# The new thread might finish before the main thread prints its message.
# The output might be interleaved.

# The threading module provides a Thread class to manage threads.
# The Thread class represents an activity that is run in a separate thread of control.
# There are two ways to specify the activity: by passing a callable object to the constructor,
# or by overriding the run() method in a subclass.
# No other methods (except for the constructor) should be overridden in a subclass.
# In other words, only override the __init__() and run() methods of this class.

# The constructor should always be called with keyword arguments.
# Arguments are:


