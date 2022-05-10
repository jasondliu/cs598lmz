import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from the other thread\n")).start()

# This is the main thread.
print("Hello from the main thread")

# The output of this program is:
# Hello from the main thread
# Hello from the other thread

# The main thread creates a new thread and then exits.
# The new thread prints a message, but the program as a whole never exits because the new thread is still running.
# The output is unpredictable because the two threads are running in parallel.
# The output might look like this:
# Hello from the main thread
# Hello from the other thread
# Or it might look like this:
# Hello from the other thread
# Hello from the main thread
# Or it might look like this:
# Hello from the main thread
# Hello from the other thread
# Hello from the main thread
# Or it might look like this:
# Hello from the other thread
# Hello from the main thread
# Hello from the other thread
# Or it might look like this:
# Hello from the other thread
# Hello from the main thread
# Hello from the other thread
# Hello from the
