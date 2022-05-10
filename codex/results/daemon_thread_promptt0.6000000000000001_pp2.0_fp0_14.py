import threading
# Test threading daemon
# if we want to use Threading, we must set the daemon attribute to True

def worker():
    print('I am a worker')
    t = threading.current_thread()
    time.sleep(3)
    print(t.getName())

new_t = threading.Thread(target=worker, name='TestThread')
new_t.setDaemon(True)
new_t.start()
time.sleep(2)
print('end')

# if we set the daemon attribute to False, the program will not end, because the main thread is waiting for the new_t thread.
# if we set the daemon attribute to True, the program will end, because the main thread will not wait for the new_t thread.

# threading.current_thread() is a method to get the current thread.

# threading.Thread.setName(name) is a method to set the name of a thread.

# threading.Thread.getName() is a method to get the name of a thread.
# we can use it to get the name of current thread.

# threading.
