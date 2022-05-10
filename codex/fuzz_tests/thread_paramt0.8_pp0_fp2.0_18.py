import sys, threading
threading.Thread(target=lambda: sys.stdout.write(\
threading.currentThread().getName()+'\n'))\
.start()

# The preceding statement is equivalent to the following code:

def fn():
    sys.stdout.write(threading.currentThread().getName()+'\n')
    
threading.Thread(target=fn).start()

#########
# daemon=True
#########

# if True, the thread is marked as a daemon thread, and the program
# will exit when the main thread exits without waiting for the daemon
# thread to terminate.

# the default value is False.

# for example

"""
threading.Thread(target=fn, daemon=True).start()

# or

t = threading.Thread(target=fn)
t.daemon = True
t.start()

"""

# Daemon threads cannot create new threads
# s = threading.Thread(target=fn, daemon=True)
# s.start()
# s.start() # error

# the thread.daemon property can be changed only before the thread
