import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start()

# Output: Hello world
# Note that the output is not printed immediately.
# The thread is started and the program exits.
# When the thread finishes, the Python interpreter exits.

# This is a simple way to launch a second thread of control.
# The thread executes the function with the argument list args (which defaults to ()).
# The thread exits when the function returns; the return value is ignored.
# The executed function must be a callable object.
# A thread can be flagged as a “daemon thread”.
# The significance of this flag is that the entire Python program exits when only daemon threads are left.
# The initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False.
# The entire Python program exits when no alive non-daemon threads are left.

# The arguments are the same as those for the Thread constructor.
# The thread implicitly calls the function with the argument list args (which defaults to ()).
# When the function returns, the thread silently exits.
