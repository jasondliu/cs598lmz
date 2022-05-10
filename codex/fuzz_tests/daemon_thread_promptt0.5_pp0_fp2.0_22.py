import threading
# Test threading daemon

def worker():
    print("I am a worker")
    t = threading.current_thread()
    print(t.getName())

new_t = threading.Thread(target=worker, name="worker_thread")
# new_t.setDaemon(True)

new_t.start()

print("Main thread")
print(threading.current_thread().getName())

 

# Test threading lock

# threading lock

lock = threading.Lock()

def worker():
    lock.acquire()
    print("I am a worker")
    t = threading.current_thread()
    print(t.getName())
    lock.release()

new_t = threading.Thread(target=worker, name="worker_thread")
# new_t.setDaemon(True)

new_t.start()

print("Main thread")
print(threading.current_thread().getName())

print("Main thread")
print(threading.current_thread().getName())

print("Main thread")
print
