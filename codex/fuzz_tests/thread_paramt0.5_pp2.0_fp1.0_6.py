import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()

# Prints "hello" in the background

# Note that the thread will be terminated when the main program exits.
# To prevent this, you can use a daemon thread:

threading.Thread(target=lambda: sys.stdout.write("hello\n"), daemon=True).start()

# To wait until a thread has completed its work, use the join() method.
# For example:

thread = threading.Thread(target=lambda: sys.stdout.write("hello\n"))
thread.start()
thread.join()

# Note that if you call join() within the target function, the threading.Thread object will deadlock;
# it will wait for itself to terminate.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
