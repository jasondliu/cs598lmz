import threading
# Test threading daemon

def run():
    print("Thread running...")
    time.sleep(3)
    print("Thread exiting...")

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

print("Main thread exiting...")

# Test threading lock

lock = threading.Lock()

def run():
    lock.acquire()
    print("Thread running...")
    time.sleep(3)
    print("Thread exiting...")
    lock.release()

t = threading.Thread(target=run)
t.start()

print("Main thread exiting...")
# Test threading lock

lock = threading.Lock()

def run():
    lock.acquire()
    print("Thread running...")
    time.sleep(3)
    print("Thread exiting...")
    lock.release()

t = threading.Thread(target=run)
t.start()

print("Main thread exiting...")

# Test threading events

e = threading.Event()

def run():

