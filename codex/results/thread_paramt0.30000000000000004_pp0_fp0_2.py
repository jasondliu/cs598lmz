import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello world\n')).start()

# The threading module has been available since Python 1.5.2.
#
# The threading module provides, among other things, a Thread class which
# contains a run() method. To create a thread, you have to subclass the Thread
# class and redefine the run() method in the subclass to implement what the
# thread should do when started.
#
# The run() method is the entry point for a thread.
#
# The following example demonstrates the simplest way to use a Thread class.
#
# The output is the following.
#
# Hello world
#
# The threading module also provides a Thread class which can be used to wrap
# a function and make it run in a separate thread.
#
# The following example demonstrates the simplest way to use a Thread class to
# wrap a function.
#
# The output is the following.
#
# Hello world
#
# The threading module also provides a Timer class which can be used to wrap
# a function and make it run in a separate thread after a specified number of
# seconds
