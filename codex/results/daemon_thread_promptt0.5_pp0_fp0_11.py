import threading
# Test threading daemon

def worker():
    print("worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
