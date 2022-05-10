import threading
# Test threading daemon
# Reference: https://docs.python.org/3/library/threading.html
def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
