import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print("Done.")

# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

def worker():
    print("Worker")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()
    threads.append(t)

print("Done.")

# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

def worker():
    print("Work
