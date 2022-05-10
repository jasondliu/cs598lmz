import threading
# Test threading daemon
# https://stackoverflow.com/questions/19058106/python-threading-daemon-vs-non-daemon

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
