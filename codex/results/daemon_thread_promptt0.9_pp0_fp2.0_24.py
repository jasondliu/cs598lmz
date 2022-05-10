import threading
# Test threading daemon usage
# https://en.wikipedia.org/wiki/Daemon_(computing)
# http://www.tutorialspoint.com/python/python_multithreading.htm
# http://www.slideshare.net/pythonexperts/multithreading-in-python
# https://pymotw.com/2/threading/

# https://docs.python.org/2/library/threading.html
# The documentation tells you that nothing is required. Actually that is not
# true, if you want to be able to kill a thread, you have to pass to the
# constructor the keywork 'daemon' set to true. That is the only case where
# you have to explicitly use this keyword in order to pass somewhere an
# argument to the thread constructor. If daemon is set to false, whenever
# the main program stops and all the other threads stop, this thread keeps
# going around execution, making the program incapable of stopping.


def worker():
    """thread worker function"""
    print 'Worker'
    return


threads = []
for i in range(5):
   
