import threading
threading.current_thread()

from threading import Thread
import time
from datetime import datetime

def myfunction(x):
    print("This is myfunction in thread %s" % threading.current_thread())
    time.sleep(4)
    print("Start time %s" % datetime.now())
    return x * 3

def f():
    res = 0
    for i in myfunction(range(0, 1000000)):
        res += i
    print(res)
    return res

thread = Thread(target=f)

thread.start()

print("This is threading.current_thread() outside of myfunction %s" % threading.current_thread())

print("Done waiting!!!")

thread.join()

# The join() method waits until the thread has completed its task.
print("thread has done!")
