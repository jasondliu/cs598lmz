import threading
# Test threading daemon
db = threading.Thread(target=my_func, args=(1, 2))
db.setDaemon = False
db.start()



"""
In order to simulate a thread-like behavior, we can use the multiprocessing library from the standard library. 
The multiprocessing library was inspired by the threading library but uses separate processes instead of threads. The main difference is that threads can communicate with each other using shared variables, but sharing variables between processes is much more complex (and requires the use of multiple shared variables).

The mp library provides a thread-like interface for processes. 
The only difference is that the Process class has a start method instead of a run method, and join has to be called explicitly on the process we want to wait for. 
"""
from multiprocessing import Process, Queue

def my_func(x, y, queue):
    """
    Returns the value of the expression
    x+y
    """
    result = x + y
    queue.put(result)
    return result

queue = Queue()
p = Process(target=my_func, args=(1,
