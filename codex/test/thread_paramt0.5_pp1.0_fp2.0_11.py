import sys, threading
threading.Thread(target=lambda:sys.stdout.write("Hello, world!\n")).start()

# The following is a script that will run in a separate thread.
# The thread will start and run in parallel with the main thread.
# The main thread will then print "Hello, world!" and exit.

# The code is not so much a trick as it is a fun way to write a thread.
# The lambda is the thread target.
# The thread target is the function the thread will run.
# The lambda is an anonymous function.
# The lambda has no name and can be used only once.
# The lambda is defined to take no arguments.
# The lambda is defined to return the value of sys.stdout.write("Hello, world!\n")
# The lambda is defined to return the value of the last expression in the function.
# The lambda is defined to return the value of the sys.stdout.write call.
# The lambda is defined to return the value of the sys.stdout.write call's return value.
# The sys.stdout.write call returns the number of characters written.
# The lambda is defined to return the value
