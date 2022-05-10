import threading
# Test threading daemon
def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping')
    
start = time.time()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.daemon = True
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
    
finish = time.time()

print(f'Finished in {round(finish-start, 2)} second(s)')

# Multiprocessing
import multiprocessing
# Multiprocessing

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')
    
start = time.time()

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
