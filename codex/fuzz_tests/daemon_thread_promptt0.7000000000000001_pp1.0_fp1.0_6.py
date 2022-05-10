import threading
# Test threading daemon
# it will close as soon as main thread ends
# daemon thread
def test():
    print("Test threading")
    time.sleep(1)

t = threading.Thread(target=test, name="Test thread")
t.setDaemon(True)
t.start()
print("Main thread")

# find running threads
running_threads = threading.enumerate()

# thread synchronization
# lock, mutex
# wait(), notify(), notify_all()

# there is more to discover
# threading module
# queue module
# asyncio module

# GIL - python global interpreter lock
# only one thread can process at a time
# other threads wait for GIL to be free
# GIL is released after 500 instructions
# and this does not mean that another thread
# can run at that time
# it can be released for other threads
# but the next one to run is the same
# that it was before, unless it ends


# python multiprocessing
# multiprocessing is used for system resources
# each process has its own memory space
# and can not access
