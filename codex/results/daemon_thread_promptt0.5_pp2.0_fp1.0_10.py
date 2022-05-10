import threading
# Test threading daemon
def task(name):
    print(f'{name} is running')
    time.sleep(2)
    print(f'{name} is done')

t = threading.Thread(target=task, args=('t1',))
t.setDaemon(True)
t.start()

print(f'{threading.current_thread().getName()} is running')
t.join()
print(f'{threading.current_thread().getName()} is done')

# The task t1 is done, the main thread is dead.

# Now we use non-daemon threading
t = threading.Thread(target=task, args=('t1',))
t.start()

print(f'{threading.current_thread().getName()} is running')
t.join()
print(f'{threading.current_thread().getName()} is done')

# The task t1 is done, the main thread is still alive.

# Now we use thread pool
# Create thread pool
with concurrent.futures.ThreadPool
