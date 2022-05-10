import sys, threading
threading.Thread(target=lambda:sys.stdout.write('hi\n'), args=()).start()
print('hello')
</code>
So, how does a Thread know what semaphore its competing for?  You need to pass that information to a Thread when it is created (as you do with the thread Target, args and kwargs).
get_lock() is just one case of this.  Calling a class method on some object reference that you have is another.
hope this helps.

