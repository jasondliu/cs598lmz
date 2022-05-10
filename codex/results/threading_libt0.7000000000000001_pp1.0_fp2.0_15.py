import threading
threading.stack_size(67108864) # 64MB stack

def thread_func():
    print('thread function')
    return

thread = threading.Thread(target=thread_func)
thread.start() 

print('thread finished...exiting')
 
# thread function
# thread finished...exiting

# https://docs.python.org/3.7/library/threading.html#thread-objects

# The class defines the following instance variables and methods.
# Instance variables:
# 
# Thread.name: the thread’s name
# Thread.daemon: whether the thread is a daemon thread
# Thread.ident: the thread identifier, a nonzero integer
# Thread.isAlive(): whether the thread is alive
# Thread.isDaemon(): whether the thread is a daemon thread
# Thread.is_alive(): whether the thread is alive
# Thread.join([timeout]): wait until the thread terminates
# Thread.run(): invoke the thread’s run method
# Thread.start(): start the thread’s activity
# Thread.ident
# The thread
