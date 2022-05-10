import sys, threading
threading.Thread(target=lambda: sys.stdout.write('test')).start()
# -> test

# This can be used to add a function to the event queue.
import queue
def func(arg):
    print(arg)
queue.Queue().put(func)
queue.Queue().put('foo')
# -> foo

# This can be used to put a task on a queue
import queue
def func(arg):
    print(arg)
queue.Queue().put((func, 'foo'))
# -> foo

# This can be used to put a task on a queue
import queue
def func(arg):
    print(arg)
queue.Queue().put((func, 'foo'))
# -> foo

# This can be used to bypass a try/except
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('test')).start()
# -> test

# This can be used to bypass a try/except
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('test')).start()
# -> test

# This
