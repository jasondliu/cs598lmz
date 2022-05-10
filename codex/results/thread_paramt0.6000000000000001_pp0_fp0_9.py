import sys, threading
threading.Thread(target=lambda:sys.stdout.write("hello ")).start()
threading.Thread(target=lambda:sys.stdout.write("world\n")).start()

################################################################################
# 21.8.2.2. Thread Objects #####################################################
################################################################################

# The constructor for the Thread class takes a callable object to be executed
# and optional arguments to the callable.
# The callable is called with those arguments in a separate thread of control.
# The callable is called in a new thread of control, which is either the main
# thread or a new thread created by the Python interpreter as needed to execute
# all threads.
# The optional arguments are packed into a tuple and passed to the callable.
# The return value of the callable is ignored, but exceptions raised in the
# callable are propagated to the caller.

# The Thread class is a subclass of the Threading.Thread class.
# This class provides a constructor that takes a callable object and optional
# arguments, and an instance method, run(), that calls the callable object.
# The constructor starts a new thread of control that calls the run()
