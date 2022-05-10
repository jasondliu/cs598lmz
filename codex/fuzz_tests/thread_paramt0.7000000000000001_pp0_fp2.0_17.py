import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread\n")).start()
print("main")

## main
## thread

# https://docs.python.org/3/library/threading.html#threading.Thread.start
# In this example the thread will run in the background while the main program continues to run.

# The thread will stop when the function returns.
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread\n")).start()
while True:
    pass

##

# The thread will stop when the program stops.
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread\n")).start()

## thread
## thread
## thread
## thread
## ...

# https://docs.python.org/3/library/threading.html#threading.Thread.start
# The default constructor for the Thread class.
# The default constructor invokes the base class constructor with the same arguments.

# The Thread class constructor.
# The constructor should invoke the base class constructor with the same
