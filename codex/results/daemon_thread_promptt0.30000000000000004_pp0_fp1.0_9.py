import threading
# Test threading daemon

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

print("Done")

# Test multiprocessing

import multiprocessing

def worker(num):
    print("Worker: ", num)
    return

if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
