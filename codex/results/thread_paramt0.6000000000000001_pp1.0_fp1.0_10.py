import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread\n')).start()

# By default, all threads created with the threading module use the same global interpreter lock (GIL) that Python uses to synchronize access to the interpreter. This means that only one thread can be in the interpreter at a time. The GIL is necessary to avoid race conditions and inconsistent data in multithreaded programs, but it also means that threads are only useful for concurrent I/O. If you want to do parallel processing, the multiprocessing module is more appropriate.

# To start a new thread, you instantiate a Thread object and pass it a function and a list containing the arguments to that function. The function is then executed concurrently in a separate thread of control.

def hello(name):
    sys.stdout.write('Hello %s\n' % name)

threading.Thread(target=hello, args=('bob',)).start()

# The Thread class has some useful methods, such as start() and join(), which are covered in more detail later.

# The Threading module also provides a Timer class, which allows you to execute a function after a specified period
