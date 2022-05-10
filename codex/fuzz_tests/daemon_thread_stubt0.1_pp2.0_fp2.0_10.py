import sys, threading

def run():
    print("Hello from new thread")

t = threading.Thread(target=run)
t.start()

print("Hello from main thread")

# Hello from main thread
# Hello from new thread

# The main thread creates a new thread and then waits for it to finish.
# The new thread runs the function run(), which prints a message.
# The main thread then prints another message.

# The output is not guaranteed to be in the order shown, because the new thread might not start immediately.
# The output could be:

# Hello from new thread
# Hello from main thread

# or

# Hello from main thread
# Hello from new thread

# or even

# Hello from new thread
# Hello from new thread
# Hello from main thread

# The last example is possible because the new thread might run to completion before the main thread gets a chance to print its message.

# The threading module provides a Thread class to manage threads.
# The Thread class represents an activity that is run in a separate thread of control.
# There are two ways to specify the activity: by passing a callable object to
