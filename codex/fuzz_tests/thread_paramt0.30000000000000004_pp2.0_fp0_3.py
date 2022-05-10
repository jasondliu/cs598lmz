import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

# Threads share global memory space with the main thread
some_var = 0

def increment_global():
    global some_var
    some_var += 1

def task_of_thread():
    for _ in range(100000):
        increment_global()

thread1 = threading.Thread(target=task_of_thread)
thread2 = threading.Thread(target=task_of_thread)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(some_var)

# Locks
some_var = 0
lock = threading.Lock()

def increment_global():
    global some_var
    lock.acquire()
    some_var += 1
    lock.release()

def task_of_thread():
    for _ in range(100000):
        increment_global()

