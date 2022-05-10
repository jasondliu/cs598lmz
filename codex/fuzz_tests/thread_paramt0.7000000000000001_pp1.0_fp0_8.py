import sys, threading
threading.Thread(target=lambda:sys.stdout.write("Hello world!\n")).start()

# 2.
import threading
def thread_function():
    for i in range(10):
        print(i)

threading.Thread(target=thread_function).start()

# 3.
import threading
def thread_function():
    for i in range(10):
        print(i)

thread = threading.Thread(target=thread_function)
thread.start()
thread.join()

# 4.
import threading
def thread_function():
    for i in range(10):
        print(i)

thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# 5.
import threading
lock = threading.Lock()
def thread_function():
    lock.acquire()
    for i in range(10):
        print(i)
    lock.release()

