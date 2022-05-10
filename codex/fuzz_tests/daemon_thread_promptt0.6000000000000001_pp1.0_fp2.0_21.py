import threading
# Test threading daemon
def worker():
    """thread worker function"""
    print ('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print ("Exiting Main Thread")
