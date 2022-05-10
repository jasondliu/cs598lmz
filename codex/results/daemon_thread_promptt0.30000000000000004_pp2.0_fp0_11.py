import threading
# Test threading daemon
import time

def worker():
    print("I am a worker")
    time.sleep(5)
    print("I am done")

t = threading.Thread(target=worker)
t.daemon = True
t.start()
print("I am main")

# Test threading join
import threading
import time

def worker():
    print("I am a worker")
    time.sleep(5)
    print("I am done")

t = threading.Thread(target=worker)
t.start()
t.join()
print("I am main")

# Test threading lock
import threading
import time

lock = threading.Lock()

def worker():
    lock.acquire()
    print("I am a worker")
    time.sleep(5)
    print("I am done")
    lock.release()

t = threading.Thread(target=worker)
t.start()
t.join()
print("I am main")

# Test threading semaphore
import threading
import time

semaphore
