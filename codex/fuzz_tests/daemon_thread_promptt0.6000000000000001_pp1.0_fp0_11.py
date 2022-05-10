import threading
# Test threading daemon
def my_worker():
    print('Starting')
    time.sleep(0.1)
    print('Exiting')
threads = list()
for i in range(5):
    t = threading.Thread(target=my_worker)
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

print('Done')

# Test multiprocessing daemon
def my_worker():
    print('Starting')
    time.sleep(0.1)
    print('Exiting')
workers = list()
for i in range(5):
    p = multiprocessing.Process(target=my_worker)
    p.start()
    workers.append(p)
for worker in workers:
    worker.join()

print('Done')
# Test multiprocessing daemon
def my_worker():
    print('Starting')
    time.sleep(0.1)
    print('Exiting')
workers = list()
for i in range(5):
    p = multiprocessing.Process(target=my_worker
