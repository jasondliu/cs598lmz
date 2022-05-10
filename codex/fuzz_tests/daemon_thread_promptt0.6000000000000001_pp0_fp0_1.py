import threading
# Test threading daemon
import time

# Define a function for the thread
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print "Error: unable to start thread"

while 1:
    pass

# The threading module
# The threading module constructs higher-level threading interfaces on top of the lower level _thread module.
# The threading module exposes all the methods of the _thread module and provides some additional methods −
#
# Thread − This is an important class of the threading module and is a class that represents an activity that runs in a separate thread of control.
#
# Lock − This is used to ensure that only one of several threads can access some
