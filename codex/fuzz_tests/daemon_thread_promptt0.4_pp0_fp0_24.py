import threading
# Test threading daemon

def worker():
    print("I am worker")
    time.sleep(10)
    print("worker is done")

thread = threading.Thread(target=worker)
thread.daemon = True
thread.start()

print("Main thread")

time.sleep(5)
print("Main thread is done")
